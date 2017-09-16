'''word pairing German:English
1) pop up or gui [PyQt]
2) verbs, adrektives, noms
    -> create choice first
3) add a word by user
4) once guessed removed -> should pop back? #if i > guessi: dic.append( guessed.pop(0) )
5) mistake correction showing -> 1. fuzzy string matching, 2. suggest corrections
6) __str__ method for the class
7) normalize the input

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

from fuzzywuzzy import fuzz
from random import randint

def random_pick(tbl):
    return randint(0, len(tbl) - 1)

def load_from_file(inp):
    tbl = []
    for line in inp:
        tbl.append(line)
    return tbl

def norm_word(word):
    return word.strip().lower()

def find_match(tbl, inp):
    ratio, match_word = 0, ''
    for word in tbl:
        temp = fuzz.ratio(inp, word)
        if temp > ratio: ratio, match_word = temp, word
    return ratio, match_word

def make_sugest(word, i, ans):
    l = len(word)
    if not ans  : ans = list(l*"*")
    if     i > 2: return "*help limit reached*\n"

    if   (i == 0): r = 0
    elif (i == 1): r =-1
    else         : r = randint(1, l-2)
    ans[r] = word[r]
    return ans

class Word:
    def __init__(self, line):
        words = line.split()
        self.en = words[1:]
        self.de = words[0]

#types   = int( input("\n1.verben\n2.nomen\npick: ") )
#turns   = int( input("Amount of turns: ") )
types   = 1
turns   = 1
points  = 0
guessed = []

if   (types == 1): dic = load_from_file( open('germ_eng.txt' , 'r') )
elif (types == 2): dic = load_from_file( open('germ_noms.txt', 'r') )

for i in range(turns):
    suggest = []
    helps   = 0
    guesses = 4
    r    = random_pick(dic)
    word = Word(dic[r])

    while guesses > 0:
        answer = norm_word( input(word.de + " in English: ") )
        if   (answer == '!'):
            print ("*answer: " + word.de + '*\n')
            break
        elif (answer == '>'):
            print('*word changed*\n')
            break
        elif (answer == '?'):
            suggest = make_sugest(word.en[0], helps, suggest)
            helps += 1
            print('to '+''.join(suggest), '\n')

        ratio, match_word = find_match(word.en, answer)
        if ratio == 100:
            guessed.append( dic.pop(r) )
            points += 1
            print('*correct*\n','points:', points,'\n')
            break
        else:
            guesses -= 1
            points  -= 1
            print('*wrong*\n')
