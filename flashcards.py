'''word pairing German:English
1) pop up or gui [PyQt]
2) verbs, adrektives, noms
    -> create choice first
    -> within the class of verbs -> dat, akk, so on
3) once guessed removed -> should pop back? (appending needed or not)
4) point counter %
5) add a word by user
6) mistake correction showing
-> compare letter by letter, not just equal and if small differences, then adjust
7) suggestions
-> take answer, show first and last letter and _

Groups:
    verbs - many answers, dat/akk choice
    noms  - der/die/das, plural
    adjektive + special words
'''
#language = int( input( "1.German:English\n2.English:German\n3.Both\n" ) )

#class Verb(Word):git
#    ''' Verb type: 1.Nom 2.Dat 3.Akk 4.Dat+Akk '''
#    def Vtype(Vtype):
#        self.type = Vtype

from random import randint

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    else:
        return -1

def random(tbl):
    return randint(0, len(tbl) - 1)

def load_from_file(inp):
    tbl = []
    for line in inp:
        tbl.append(line)
    return tbl

def make_sugest(word):
    #1 question-> lenght and first letter, then last letter, then random letter
    ans = word[0]
    print (ans[0]+(len(ans)-2)*"*"+ans[-1])

class Word:
    def __init__(self, line):
        words = line.split()
        self.de = words[0]
        self.en = words[1:]

#class Nom:
#    def __init__(self, line):
#        words = line.split()
#        self.de  = words[0]
#        self.en  = words[2:]
#        self.gen = words[1]

DIC     = load_from_file( open('germ_eng.txt' , 'r') )
DIC_nom = load_from_file( open('germ_noms.txt', 'r') )
guessed = []

types   = int( input("\n1.verben\n2.nomen\npick: ") )
turns   = int( input("Amount of turns: ") )

if (types == 1):
    dictionary = DIC
elif (types == 2):
    dictionary = DIC_nom

for i in range(turns):
    guesses_left = 3
    r    = random( dictionary )
    word = Word  ( dictionary[r] )

    while guesses_left > 0:
        answer = input(word.de + " in English: ")
        if( answer.lower() in word.en ):
            print('correct\n')
            guessed.append( DIC.pop(r) )
            break
        elif( answer.lower() == "?"):
            d = make_sugest(word.en)
            print( d, '\n' )
        else:
            guesses_left -= 1
            print('wrong\n')
