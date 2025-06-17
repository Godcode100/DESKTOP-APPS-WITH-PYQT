import sys
from PyQt6.QtWidgets import (QApplication,QMessageBox,QPushButton,QLabel,QDialog,QLineEdit)
from PyQt6.QtGui import QFont,QPixmap

class NewUserDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(360,320)
        self.setWindowTitle("Register Here")
        self.setUpMainWindow()

    def setUpMainWindow(self):
        create_account_label = QLabel("Create User Account",self)
        create_account_label.setFont(QFont("Arial",20))
        create_account_label.move(90,20)

        user_image = "images/new_user_icon.png"
        try:
            with open(user_image):
                user_labe = QLabel(self)
                pixmap = QPixmap(user_image)
                user_labe.setPixmap(pixmap)
                user_labe.move(150,60)
        except FileNotFoundError as error:
            print(f"Image Not Found. Error {error}")

        name_label = QLabel("Username",self)
        name_label.move(20,144)

        self.name_label_edit =QLineEdit(self)
        self.name_label_edit.resize(250, 24)
        self.name_label_edit.move(90, 140)

        fullname_label = QLabel("Fullname",self)
        fullname_label.move(20, 174)

        fullname_label_edit = QLineEdit(self)
        fullname_label_edit.resize(250, 24)
        fullname_label_edit.move(90, 170)

        passwd_label = QLabel("Password:",self)
        passwd_label.move(20, 204)

        self.passwd_label_edit =QLineEdit(self)
        self.passwd_label_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwd_label_edit.resize(250, 24)
        self.passwd_label_edit.move(90, 200)

        confirm_passwd_label = QLabel("Confirm Password:",self)
        confirm_passwd_label.move(20, 234)
        
        self.confirm_passwd_label_edit = QLineEdit(self)
        self.confirm_passwd_label_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_passwd_label_edit.resize(250, 24)
        self.confirm_passwd_label_edit.move(90,230)

        sign_up_button =QPushButton("Sign Up",self)
        sign_up_button.resize(320, 32)
        sign_up_button.move(20,270)
        sign_up_button.clicked.connect(self.confirmSignUp)

    def confirmSignUp(self):
        name = self.name_label_edit.text()
        password = self.passwd_label_edit.text()
        confirm_password = self.confirm_passwd_label_edit.text()

        if name== "" or password == "":
            QMessageBox.warning(self,"Error",
                                "Please Usrname or Password",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        elif password != confirm_password:
            QMessageBox.warning(self,"Error",
                                "The Passwords entered do not much",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
            
        else:
            with open("users.txt", "a+") as f:
                f.write("\n" + name + " ")
                f.write(password)
            self.close()


