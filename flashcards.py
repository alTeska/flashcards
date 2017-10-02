from fuzzywuzzy import fuzz
from random     import randint

def random_pick(tbl):
    return randint(0, len(tbl) - 1)

def load_from_file(inp):
    tbl = []
    for line in inp:
        tbl.append(line)
    return tbl

def norm_word(word):
    return word.strip().lower()

def make_sugest(word, i, ans):
    l = len(word)
    if not ans  : ans = list(l*"*")
    if     i > 2: return "*help limit reached*\n"

    if   (i == 0): r = 0
    elif (i == 1): r =-1
    else         : r = randint(1, l-2)
    ans[r] = word[r]
    return ans

def find_match(inp, ans): #fix: down to letters
    ratio, match_word = 0, ''
    if ( isinstance(ans, str) ): ratio = fuzz.ratio(inp, ans)
    else:
        for word in ans:
            temp = fuzz.ratio(inp, word)
            if temp > ratio: ratio, match_word = temp, word
    return ratio, match_word

class Verb(object):
    chances = 3
    def __init__(self, line):
        words = line.split()
        self.en = words[1:]
        self.de = words[0]

    def check_answer(self, inp, ans):
        ratio, match_word = find_match(inp, ans)
        if ratio == 100:
            print('*correct*\n')
            self.chances = 0
        elif ratio >= 90:
            print (match_word)
        else:
            print('*wrong*\n')
        self.chances -= 1

    def play_round(self, way):
        if   way == 0: translate, answer = self.de, self.en
        else         : translate, answer = self.en[0], self.de

        while self.chances > 0:
            inp = norm_word( input(translate + " translate: ") ) #str matching
            self.check_answer(inp, answer)


turns   = 1 #int( input("Amount of turns: ") )
types   = 1
points  = 0
guessed = []

transl_dir = 1

if   (types == 1): dic = load_from_file( open('germ_eng.txt' , 'r') )
elif (types == 2): dic = load_from_file( open('germ_noms.txt', 'r') )

for i in range(2):
    rand = random_pick(dic)
    word = Verb( dic[rand] )

    word.play_round( transl_dir )
    guessed.append ( dic.pop(rand) )
