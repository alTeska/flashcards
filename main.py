##main 1
import sys
#from GUI import *
from flashcards import *
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
        self.inp = self.textInp.text()
        self.word.check_ans(self.inp)
        #self.textOut.setText(ans)

    def game_round(self, dic, Word, trDir, types):
        rand = random_pick( dic )
        self.word = Word( dic[rand] )
        self.word.pick_dir( trDir )

        self.textOut.setText(word_print(self.word, trDir, types))
        dic.pop( rand )

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = Application()

   points = 0
   types = 0
   trDir = 1
   guessed = []

   dic_ver = load_from_file( open('germ_verb.txt', 'r') )
   dic, Word = dic_ver, Verb

   window.game_round(dic, Word, trDir, types)
   sys.exit(app.exec_())
