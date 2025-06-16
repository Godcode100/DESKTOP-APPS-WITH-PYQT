import sys
from PyQt6.QtWidgets import (QApplication,QWidget,QPushButton,QCheckBox,QLabel)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100,100,250,150)
        self.setWindowTitle("DEMONSTRATING CHECKBOXES")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        heading_label = QLabel("Please select or deselect a \
                               check box below of your choice",self)
        heading_label.setWordWrap(True)
        heading_label.move(20,10)

        morning = QCheckBox("Morning [8 AM-2 PM]", self) 
        morning.move(40, 60)
        morning.toggle() 
        morning.toggled.connect(self.SelfPrint)

        afternoon = QCheckBox("afternoon [2 PM-11 PM]", self) 
        afternoon.move(40, 80)
        afternoon.toggled.connect(self.SelfPrint)

        night = QCheckBox("night [11 PM-6 AM]", self) 
        night.move(40, 100)
        night.toggled.connect(self.SelfPrint)

    def SelfPrint(self,check):
        sender = self.sender()
        if check:
            print(f"{sender.text()} Selected.")
        else:
            print(f"{sender.text()} Deselected.")




if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())