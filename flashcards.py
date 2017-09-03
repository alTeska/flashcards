'''word pairing German:English
1) pop up or gui
2) verbs, adrektives, noms
    -> create choice first
    -> within the class of verbs -> dat, akk, so on
3) once guessed removed -> should pop back? (appending needed or not)
4) point counter %
5) amount of turns to be chosen first

verbs - many answers, dat/akk choice
adjektive
noms  - der/die/das, plural
'''
from random import randint

def random(tbl):
    return randint(0, len(tbl) - 1)

def load_from_file(inp):
    tbl = []
    for line in inp:
        tbl.append(line)
    return tbl

class Word:
    def __init__(self, line):
        words = line.split()
        self.de = words[0]
        self.en = words[1:]

#class Verb(Word):
#    ''' Verb type: 1.Nom 2.Dat 3.Akk 4.Dat+Akk '''
#    def Vtype(Vtype):
#        self.type = Vtype

DIC     = load_from_file( open('germ_eng.txt', 'r') )
guessed = []
turns   = int(input( "Amount of turns:" ))

for i in range(turns):
    guesses_left = 3
    r = random(DIC)
    word = Word( DIC[r] )
    while guesses_left > 0:
        answer = input(word.de + " English: to ")
        if( answer in word.en ):
            print('correct\n')
            guessed.append( DIC.pop(r) )
            break
        else:
            guesses_left -= 1
            print('wrong\n')
