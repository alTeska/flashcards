import sys
from flashcards      import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.dic_ver = load_from_file( open('germ_verb.txt', 'r') )
        self.dic_nom = load_from_file( open('germ_noms.txt', 'r') )
        self.dic   = self.dic_ver
        self.Word  = Verb
        self.types = False
        self.trDir = True

        self.setWindowTitle('Flashcards')
        self.create_app()
        self.game_round(self.dic, self.Word, self.trDir, self.types)

    def create_app(self):
        grid  = QGridLayout()
        self.label = QLabel('Translate:')
        self.ansButton  = QPushButton('ans')
        self.nextButton = QPushButton('next')
        self.okButton   = QPushButton('ok')
        self.langButton = QPushButton('DE<->EN')
        self.suggButton = QPushButton('suggest')
        self.wordButton = QPushButton('wordType')
        self.textOut = QLineEdit()
        self.answer  = QLineEdit()
        self.textInp = QLineEdit()

        grid.addWidget(self.label     , 0, 0, 1, 1)
        grid.addWidget(self.langButton, 1, 0, 1, 1)
        grid.addWidget(self.wordButton, 1, 1, 1, 1)
        grid.addWidget(self.suggButton, 1, 2, 1, 1)
        grid.addWidget(self.textOut   , 2, 0, 1, 3)
        grid.addWidget(self.textInp   , 3, 0, 1, 3)
        grid.addWidget(self.okButton  , 4, 2, 1, 1)
        grid.addWidget(self.nextButton, 4, 1, 1, 1)
        grid.addWidget(self.ansButton , 4, 0, 1, 1)
        grid.addWidget(self.answer    , 5, 0, 1, 3)

        self.langButton.clicked.connect(self.lang_change)
        self.wordButton.clicked.connect(self.type_change)
        self.suggButton.clicked.connect(self.suggest_ans)

        self.nextButton.clicked.connect(self.next_click)
        self.okButton.clicked.connect(self.check_click)
        self.ansButton.clicked.connect(self.give_ans)

        self.setLayout(grid)
        self.show()

    def check_click(self):
        self.inp = self.textInp.text()
        out      = self.word.check_ans(self.inp)
        self.answer.setText(out)

    def next_click(self):
        self.game_round(self.dic, self.Word, self.trDir, self.types)

    def suggest_ans(self):
        word = self.word
        word.suggest = make_suggest(word.ans[0], word.help_cnt,word.suggest)
        word.help_cnt += 1
        self.answer.setText(''.join(word.suggest))

    def give_ans(self):
        self.answer.setText(self.word.ans[0])

    def lang_change(self):
        self.trDir = change_state(self.trDir)
        self.game_round(self.dic, self.Word, self.trDir, self.types)

    def type_change(self):
        if   (self.types == False):
            self.types = True
            self.dic, self.Word = self.dic_ver, Verb
        elif (self.types == True):
            self.types = False
            self.dic, self.Word = self.dic_nom, Nom
        self.game_round(self.dic, self.Word, self.trDir, self.types)

    def game_round(self, dic, Word, trDir, types):
        rand = random_pick( dic )
        self.word = Word( dic[rand] )
        self.word.pick_dir( trDir )

        self.textOut.setText(word_print(self.word, trDir, types))
        #dic.pop( rand )

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = Application()
   sys.exit(app.exec_())
