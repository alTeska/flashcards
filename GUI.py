#GUI UPDATE
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *

class Application(QWidget):
    def __init__(self):
        super().__init__() #init the parent
        self.setWindowTitle('Flashcards')
        self.CreateApp()

    def CreateApp(self):
        grid  = QGridLayout()
        self.label  = QLabel('Translate:')
        self.button = QPushButton('ok')
        self.textInp = QLineEdit()
        self.textOut = QLineEdit()

        grid.addWidget(self.label  , 0, 0, 1, 1)
        grid.addWidget(self.textOut, 1, 0, 1, 1)
        grid.addWidget(self.textInp, 2, 0, 1, 1)
        grid.addWidget(self.button , 3, 0, 1, 1)

        self.button.clicked.connect(self.on_click)
        self.setLayout(grid)
        self.show()

    def on_click(self):
        ans = self.textInp.text()
        self.textOut.setText(ans)
