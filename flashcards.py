'''word pairing German:English
1) pop up or gui [PyQt]
2) verbs, adrektives, noms
    -> create choice first
3) add a word by user

4) switching the class so it uses dictionaries (already in use?)
5) once guessed removed -> should pop back?
6) mistake correction showing
-> compare letter by letter, not just equal and if small differences, then adjust
7) __str__ method for the class

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

from random import randint

def random_pick(tbl):
    return randint(0, len(tbl) - 1)

def load_from_file(inp):
    tbl = []
    for line in inp:
        tbl.append(line)
    return tbl


#to be simplified ?? def get_letter(i):
def make_sugest(word, i, ans):
    first_word = word[0]
    l = len(first_word)
    if   (i == 0):
        ans = list(l*"*")
        ans[0]  = first_word[0]
    elif (i == 1):
        ans[-1] = first_word[-1]
    elif (i > 2 ):
        return ("*help limit reached*\n")
    else:
        r = randint(1, l-2)
        ans[r] = first_word[r]
    return ans

class Word:
    def __init__(self, line):
        words = line.split()
        self.de = words[0]
        self.en = words[1:]

#types   = int( input("\n1.verben\n2.nomen\npick: ") )
#turns   = int( input("Amount of turns: ") )
types   = 1
turns   = 1
points  = 0
guessed = []
guessi  = 0

if   (types == 1): dic = load_from_file( open('germ_eng.txt' , 'r') )
elif (types == 2): dic = load_from_file( open('germ_noms.txt', 'r') )

''' conditions: no identical words
1. go thorugh 1st and 2nd word to compare -> if not then check next letter
2. first try is one by one if identical, counter if over treshhol go for it
3. missing letters (checking lenghts)
'''

#def mistake_check(word):
    #i = 0
    #while i < len(word):
    #    if word[i] == letter:
    #        return i
    #    i += 1
    #else:
    #    return -1

for i in range(turns):
    suggest = []
    helps   = 0
    guesses = 4
    r    = random_pick(dic)
    word = Word(dic[r])

    while guesses > 0:
        answer = input(word.de + " in English: ").lower()
        if   (answer in word.en):
            guessed.append( dic.pop(r) )
            points += 1
            print('*correct*\n','points:', points,'\n')
            break
        elif (answer == '?'):
            suggest = make_sugest(word.en, helps, suggest)
            helps += 1
            print('to '+''.join(suggest), '\n')
        elif (answer == '!'):
            print ("*answer: " + word.de + '*\n')
            break
        elif (answer == '>'):
            points  -= 0.5
            print('*word changed*\n')
            break
        else:
            guesses -= 1
            points  -= 1
            print('*wrong*\n')

    #different solution needed
    #if i > guessi: dic.append( guessed.pop(0) )
    #guessi=i
