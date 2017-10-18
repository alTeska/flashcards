import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Flashcards'
        self.left = 10
        self.top = 10
        self.width = 310
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Translate:")
        layout  = QGridLayout()
        self.textbox = QLineEdit(self)
        self.button = QPushButton('Show text')
        self.button.clicked.connect(self.on_click)

        #layout.setRowStretch(1, 20)
        layout.setRowMinimumHeight(1, 20)

        #layout.addWidget(QPushButton('1') ,0,0)
        layout.addWidget(self.button ,0,0)
        layout.addWidget(QPushButton('2') ,0,1)
        layout.addWidget(QPushButton('3') ,0,2)

        #layout.addWidget(QLineEdit('Word'),1,0,1,3)
        layout.addWidget(self.textbox,1,0,1,3)
        layout.addWidget(QLineEdit('')    ,2,0,1,3)
        layout.addWidget(QPushButton('ok'),3,2)
        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_click(self):
        textboxValue = textbox.text()
        QMessageBox.question('Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
