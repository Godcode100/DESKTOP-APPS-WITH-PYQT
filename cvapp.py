import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QWidget,QLabel
from PyQt6.QtGui import QFont,QPixmap

class OuterWindow(QWidget):
    def __init__(self, ) :
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50,50,250,400)
        self.setWindowTitle("DESKTOP CIRRICULUM APP")
        self.setUpMainWindow()
        self.show()

    def createLabels(self):
        images = ["images/skyblue.png","images/profile_image.png"]
        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                if image == "images/profile_image.png":
                    label.move(80,20)
            except FileNotFoundError as error:
                print(f"Image not found\n Error {error}")



    
    def setUpMainWindow(self):
        self.createLabels()
        """Create QLabel to be displayed in the main window."""
        user_name = QLabel(self)
        user_name.setText("John Doe")
        user_name.setFont(QFont("Arial", 20))
        user_name.move(85, 140)

        user_bio = QLabel(self)
        user_bio.setText("PROGRAMMING EXPRIENCE")
        user_bio.setFont(QFont("Arial", 10))
        user_bio.move(15, 170)

        user_bio_details = QLabel(self)
        user_bio_details.setText("I'm a Software Engineer with 10 years experience creating awesome code.")
        user_bio_details.setWordWrap(True)
        user_bio_details.move(15, 190)

        user_bio_skills = QLabel(self)
        user_bio_skills.setText("SKILLS")
        user_bio_skills.setFont(QFont("Arial",italic=True))
        user_bio_skills.move(15,240)

        user_programming_languages = QLabel(self)
        user_programming_languages.setText("Python | vyper | HTML | CSS | BASH")
        #languages.setFont(QFont())
        user_programming_languages.move(15,260)





if __name__== "__main__":
    app = QApplication([])
    window= OuterWindow()
    sys.exit(app.exec())
