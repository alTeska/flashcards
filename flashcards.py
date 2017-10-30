from fuzzywuzzy import fuzz
from random     import randint

#def find(word, letter):
#    index = 0
#    while index < len(word):
#        if word[index] == letter:
#            return index
#        index += 1
#    else:
#        return -1

def change_state(x):
    return False if x else True

def random_pick(tbl):
    return randint(0, len(tbl) - 1)

def load_from_file(inp):
    tbl = []
    for line in inp:
        tbl.append(line)
    return tbl

def norm_word(word):
    return word.strip().lower()

def find_match(inp, ans):
    ratio, match_word = 0, ''
    for word in ans:
        temp = fuzz.ratio(norm_word(inp), norm_word(word))
        if temp > ratio: ratio, match_word = temp, word
    return ratio, match_word

def make_suggest(ans, i, suggest):
    l = len(ans)
    if not suggest: suggest = list(l*"*")
    if     i > 2 : return "*help limit reached*\n"

    if   (i == 0): r = 0
    elif (i == 1): r =-1
    else         : r = randint(1, l-2)
    suggest[r] = ans[r]
    return suggest

def tr_print(trDir):
    if   (trDir == 0): return ('to EN')
    elif (trDir == 1): return ('to DE')

def word_print(word, trDir, types):
    if   (trDir == 0 and types == 1): return (word.art + word.tr)
    else                            : return (word.tr)

def word_print(word, trDir, types):
    return (word.tr[0])

class Word(object):
    help_cnt = 0
    chances = 3
    suggest = []

    def pick_dir(self, trDir):
        if   trDir == 0: self.tr, self.ans = self.de, self.en
        else           : self.tr, self.ans = self.en, self.de

    def check_ans(self, inp):
        ratio, match_word = find_match(inp, self.ans)
        if ratio == 100:
            return '*correct*'
            self.chances = 0
        #elif ratio >= 90: #dev
            #    print (match_word)
        else:
            return '*wrong*'
            self.chances -= 1

class Verb(Word):
    def __init__(self, line):
        words = line.split()
        self.de = [words[0]]
        self.en = words[1:]

class Nom(Word):
    def __init__(self, line):
        words = line.split()
        self.art = [words[0]]
        self.de  = [words[1]]
        self.en  =  words[2:]

    def check_art(self, art):
        ratio, match_art = find_match(art, self.art)
        if ratio == 100: print ('*correct article*')
        else           : print ('*wrong article*')
