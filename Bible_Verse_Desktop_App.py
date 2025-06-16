import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication,QWidget,QLabel,QPushButton)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        self.setGeometry(100, 100, 350, 150)
        self.setWindowTitle("A Desktop App To Generate Verses")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.times_pressed = 0

        self.name_label = QLabel("Generate Bible Verses",self)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.move(60,30)

        self.button = QPushButton("Click Here To Get Bible Verses",self)
        self.button.move(80,70)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        """Handles the Bible Verse Generation when the button is clicked. 
        Demonstrates how to change text for widgets,
        update their sizes and locations, and how to
        close the window due to events."""
        self.times_pressed += 1
        if self.times_pressed == 1:
            self.name_label.setText("Isaiah 26:3 You will Keep in Perfect Peace He whose mind is stayed on you")
            self.name_label.setWordWrap(True)
            self.name_label.adjustSize()

        if self.times_pressed == 2:
            self.name_label.setText("Ephesians 3:17 That Christ may dwell in your hearts through faith; that you being rooted and grounded in love  ")
            self.name_label.setWordWrap(True)
            self.name_label.adjustSize()
            self.button.move(70,90)
            
        if self.times_pressed == 3:
            self.name_label.setText("Psalms 11:3 The Foundations of law and order have collapsed what can the righteous do")
            self.name_label.setWordWrap(True)
            self.name_label.adjustSize()
            self.button.setText("Close This App")
            self.button.adjustSize()
            self.button.move(70,90)
        if self.times_pressed == 4:
            print("You are closing this Application")
            self.close()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
