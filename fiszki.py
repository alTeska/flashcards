'''word pairing German:English
1) pop up or gui
3) verbs, adrektives, noms
    -> create choice first
    a) within the class of verbs -> dat, akk, so on
4) once guessed removed for a while
    -> one table storage, removed to "guessed"
5) point counter %
7) backup the file, from wrong inputs -> swtich to database(?)
'''
from random import randint

#def find(word, letter):
#    index = 0
#    while index < len(word):
#        if word[index] == letter:
#            return index
#        index += 1
#    else:
#        return -1

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

DIC_file = open('germ_eng.txt' ,'r')
DIC      = load_from_file(DIC_file)

for turn in range(3):
    guesses_left = 3
    word = Word( DIC[random(DIC)] )

    while guesses_left > 0:
        answer = input(word.de + " English: to ")
        if( answer in word.en ):
            print('correct\n')
            #DIC.remove(word)
            break
        else:
            guesses_left -= 1
            print('wrong\n')
