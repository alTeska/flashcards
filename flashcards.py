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
    verbs - many answers, dat/akk choice - > Verb type: 1.Nom 2.Dat 3.Akk 4.Dat+Akk
    noms  - der/die/das, plural
    adjektive + special words
'''
#language = int( input( "1.German:English\n2.English:German\n3.Both\n" ) )

#class Nom:
#    def __init__(self, line):
#        words = line.split()
#        self.de  = words[0]
#        self.en  = words[2:]
#        self.gen = words[1]

#def find(word, letter): #not in us atm
#    index = 0
#    while index < len(word):
#        if word[index] == letter:
#            return index
#        index += 1
#    else:
#        return -1

from random import randint

def random_tbl(tbl):
    return randint(0, len(tbl) - 1)

def load_from_file(inp):
    tbl = []
    for line in inp:
        tbl.append(line)
    return tbl

def make_sugest(word, i, ans):
    first_word = word[0]
    l = len(first_word)
    if   i == 0:
        ans = list(l*"*")
        ans[0]  = first_word[0]
    elif i == 1:
        ans[-1] = first_word[-1]
    else:
        r = randint(1, l-2)
        ans[r] = first_word[r]
    return ans

class Word:
    def __init__(self, line):
        words = line.split()
        self.de = words[0]
        self.en = words[1:]

DIC     = load_from_file( open('germ_eng.txt' , 'r') )
DIC_nom = load_from_file( open('germ_noms.txt', 'r') )
guessed = []

#types   = int( input("\n1.verben\n2.nomen\npick: ") )
types   = 1
#turns   = int( input("Amount of turns: ") )
turns   = 1

if (types == 1):
    dictionary = DIC
elif (types == 2):
    dictionary = DIC_nom

for i in range(turns):
    guesses_left = 4
    help_counter = 0
    suggest = []
    r    = random_tbl( dictionary )
    word = Word( dictionary[r] )

    while guesses_left > 0:
        answer = input(word.de + " in English: ").lower()
        if ( answer in word.en ):
            print('correct\n')
            guessed.append( DIC.pop(r) )
            break
        elif ( answer == "?" ):
            suggest = make_sugest(word.en, help_counter, suggest)
            help_counter += 1
            print('to '+''.join(suggest), '\n')
        else:
            guesses_left -= 1
            print('wrong\n')
