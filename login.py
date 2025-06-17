import sys
from PyQt6.QtWidgets import (QApplication,QWidget,QCheckBox,QPushButton,QLabel,QLineEdit,QMessageBox)
from PyQt6.QtGui import QCloseEvent, QFont,QPixmap
from PyQt6.QtCore import Qt
from signup import NewUserDialog

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(360,220)
        self.setWindowTitle("Login")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.login_successful = False

        login_label = QLabel("login",self)
        login_label.setFont(QFont("Arial",20))
        login_label.move(160,10)

        username_label =QLabel("Username",self)
        username_label.move(20,54)

        self.usernames = QLineEdit(self)
        self.usernames.resize(250,24)
        self.usernames.move(90,50)

        
        passwords_label = QLabel("Password",self)
        passwords_label.move(20,82)

        self.passwords =QLineEdit(self)
        self.passwords.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwords.resize(250,24)
        self.passwords.move(90,86)

        self.show_password_cb =QCheckBox("show Password",self)
        self.show_password_cb.move(90,110)
        self.show_password_cb.toggled.connect(self.ShowPasswordIfChecked)

        login_button = QPushButton("login",self)
        login_button.resize(320,34)
        login_button.move(20,140)
        login_button.clicked.connect(self.Enterlogin)

        not_a_member_label = QLabel("Not a member?",self)
        not_a_member_label.move(20,186)

        sign_up_button = QPushButton("Sign Up",self)
        #sign_up_button.resize()
        sign_up_button.move(120,180)
        sign_up_button.clicked.connect(self.createUser)

    def Enterlogin(self):
        users = {}
        file = "users.txt"
        try:
            with open(file,"r") as f:
                for line in f:
                    user_info = line.split(" ")
                    username_info = user_info[0]
                    password_info = user_info[-1].strip("\n")
                    users[username_info]=password_info
            username=self.usernames.text()
            password =self.passwords.text()

            if (username,password) in users.items():
                QMessageBox.information(self,"Login succesful!",
                                        "Login Succesful!",
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.login_successful = True
                self.close()
                self.openApplicationWindow()
            else:
                QMessageBox.warning(self,"Error Warning",
                                    "The Username or password you entered is incorrect",
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)

        except FileNotFoundError as error:
            QMessageBox.warning(self,"Error",
                                f"""<p>No File was Found</p>
                                <p>Error:{error}</p>""",
                                QMessageBox.StandardButton.Ok)
            f = open(file,"w")

    def ShowPasswordIfChecked(self,checked):
        if checked:
            self.passwords.setEchoMode(
                QLineEdit.EchoMode.Normal)
        elif checked == False:
            self.passwords.setEchoMode(
                QLineEdit.EchoMode.Password)
                
    def createUser(self):
        self.create_user = NewUserDialog()
        self.create_user.show()

    def openApplicationWindow(self):
        self.main_window = MainWindow()
        self.main_window.show()

    def closeEvent(self,event):
        if self.login_successful == True:
            event.accept()
        else:
            answer = QMessageBox.question(self,"Quit Application",
                                          "Are you sure you want to quit this application?"\
                                          ,QMessageBox.StandardButton.Yes |\
                                          QMessageBox.StandardButton.No,\
                                          QMessageBox.StandardButton.Yes)
            if answer == QMessageBox.StandardButton.Yes:
                event.accept()
            if answer == QMessageBox.StandardButton.No:
                event.ignore()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(640, 426)
        self.setWindowTitle("Main Window")
        self.setUpMainWindow()
    
    def setUpMainWindow(self):
        image = "images/background_kingfisher.jpg"
        try:
            with open(image):
                logged_in_label = QLabel(self)
                pixmap = QPixmap(image)
                logged_in_label.setPixmap(pixmap)
                logged_in_label.move(0,0)
        except FileNotFoundError as error:
            print(f"Image Not Found\n Error:{error}")
            

if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    sys.exit(app.exec())

    