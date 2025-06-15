import os
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QListWidget,QVBoxLayout,QHBoxLayout,QFileDialog,QSlider
from PyQt6.QtCore import Qt,QTimer,QUrl
from PyQt6.QtMultimedia import QAudioOutput,QMediaPlayer


#My App
class Audioapp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        self.event_handler()

    #settings
    def settings(self):
        self.setWindowTitle("Aud-just")
        self.setGeometry(500,500,600,300)



    #Design
    def initUI(self):
        self.title = QLabel("Audio Adjuster")
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.file_list = QListWidget()
        self.btn_opener = QPushButton("Choose a file")
        self.btn_play = QPushButton("play")
        self.btn_pause = QPushButton("pause")
        self.btn_resume = QPushButton("Resume")
        self.btn_reset = QPushButton("Reset")

        #Deactivate buttons for now
        self.btn_pause.setDisabled(True)
        self.btn_resume.setDisabled(True)
        self.btn_reset.setDisabled(True)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(50)
        self.slider.setMaximum(150)
        self.slider.setValue(100)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)

        self.slider_text = QLabel("Speed 100x")
        self.slider_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        slider_layout = QHBoxLayout()
        slider_layout.addWidget(self.slider_text)
        slider_layout.addWidget(self.slider)

        #create layout
        self.master = QVBoxLayout()
        row = QHBoxLayout()
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        self.master.addWidget(self.title)
        self.master.addLayout(slider_layout)


        col1.addWidget(self.file_list)
        col2.addWidget(self.btn_opener)
        col2.addWidget(self.btn_play)
        col2.addWidget(self.btn_pause)
        col2.addWidget(self.btn_resume)
        col2.addWidget(self.btn_reset)

        row.addLayout(col1 ,2)
        row.addLayout(col2, 4)
        self.master.addLayout(row)
        self.setLayout(self.master)

        self.style()


        #special audio classes from PyQt
        self.audio_output = QAudioOutput()
        self.media_player =QMediaPlayer()
        self.media_player.setAudioOutput(self.audio_output)

    #style method
    def style(self):
        self.setStyleSheet("""

                            QWidget{
                                background-color:#F9DBBA;
                            }
                            QPushButton{
                                background-color:#5BB9C2;
                                padding:15px;
                                border-radius:9px;
                                color: #333;
                            }
                            QPushButton:hover{
                                background-color:#1A4870;
                                color: #F9DBBA;
                            }
                            QLabel{
                                color:#333;
                            }
                            #title{
                                font-family:Papyrus;
                                font-size:40px;
                           }
                            QSlider{
                                margin-right:15px;
                            }
                            QlistWidget{
                                color:#333;
                            }

                          """)

    #Event handler
    def event_handler(self):
        self.slider.valueChanged.connect(self.update_speed)
        self.btn_opener.clicked.connect(self.open_file)
        self.btn_play.clicked.connect(self.play_audio)
        self.btn_pause.clicked.connect(self.pause_audio)
        self.btn_resume.clicked.connect(self.resume_audio)
        self.btn_reset.clicked.connect(self.reset_audio)

    #change slider spedd label
    def update_speed(self):
        speed = self.slider.value() / 100
        self.slider_text.setText(f"Speed: {speed:.2f}x")

    def open_file(self):
        path = QFileDialog.getExistingDirectory(self,"Select Folder")
        if path:
            self.file_list.clear()
            for file_name in os.listdir(path):
                if file_name.endswith(".mp3"):
                    self.file_list.addItem(file_name)
        else:
            file,_ = QFileDialog.getOpenFileName(self,"Select file",filter="Audio Files(*.mp3)")
            if file:
                self.file_list.clear()
                self.file_list.addItem(os.path.basename(file))

    #Audio play
    def play_audio(self):
        if self.file_list.selectedItems():
            file_name = self.file_list.selectedItems()[0].text()
            folder_path = QFileDialog.getExistingDirectory(self,"Select folder")
            file_path = os.path.join(folder_path,file_name)
            fileurl = QUrl.fromLocalFile(file_path)

            self.media_player.setSource(fileurl)
            self.media_player.setPlaybackRate(self.slider.value() /100.0)
            self.media_player.play()

            self.btn_pause.setEnabled(True)
            self.btn_resume.setEnabled(True)
            self.btn_reset.setEnabled(True)
            self.btn_play.setDisabled(True)

    def pause_audio(self):
        self.media_player.pause()
        self.btn_pause.setDisabled(True)
        self.btn_resume.setEnabled(True)

    def resume_audio(self):
        self.media_player.play()
        self.btn_pause.setEnabled(True)
        self.btn_resume.setDisabled(True)

    def reset_audio(self):
        if self.media_player.isPlaying():
            self.media_player.stop()
        self.media_player.setPosition(0)
        self.media_player.setPlaybackRate(self.slider.value() / 100.0)
        self.media_player.play()

        self.btn_pause.setEnabled(True)
        self.btn_resume.setDisabled(True)
        self.btn_reset.setDisabled(True)
        self.btn_play.setDisabled (True)

        QTimer.singleShot(100, lambda:self.btn_reset.setEnabled(True))


#Boilerplate
if __name__ in "__main__":
    app = QApplication([])
    main = Audioapp()
    main.show()
    app.exec()