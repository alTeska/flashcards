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

def find_match(inp, ans):
    ratio, match_word = 0, ''
    if ( isinstance(ans, str) ):
        return fuzz.ratio(inp, ans), ans
    else:
        for word in ans:
            temp = fuzz.ratio(inp, word)
            if temp > ratio: ratio, match_word = temp, word
    return ratio, match_word

def check_ans(inp, ans, chances):
    ratio, match_word = find_match(inp, ans)
    if ratio == 100:
        print ('*correct*\n')
        return 0
    elif ratio >= 90: #dev
        print (match_word)
    else:
        print ('*wrong*\n')
    return chances - 1

def translate(transl, ans, chances, way):
    while chances > 0:
        inp     = norm_word( input(transl + " translate %s: " % way) )
        chances = check_ans(inp, ans, chances)

class Verb(object):
    chances = 3
    def __init__(self, line):
        words = line.split()
        self.de = words[0]
        self.en = words[1:]

    def transl_round(self, way):
        if   way == 0: transl, ans = self.de   , self.en
        else         : transl, ans = self.en[0], self.de
        translate(transl, ans, self.chances, way)

class Nom(object):
    chances = 3
    def __init__(self, line):
        words = line.split()
        self.art = words[0]
        self.de  = words[1]
        self.en  = words[2:]

    def transl_round(self, way):
        if   way == 0: transl, ans = self.de   , self.en
        else         : transl, ans = self.en[0], (self.art + ' ' + self.de)
        translate(transl, ans, self.chances, way)

def game_round(dic, Word, transl_dir):
    rand = random_pick(dic)
    word = Word( dic[rand] )
    word.transl_round( transl_dir )
    dic.pop( rand )

turns      = 1   #int( input("Amount of turns: ") )
types      = 1   #int( input("\n1.verben\n2.nomen\npick: ") )
points     = 0
transl_dir = 0   #int( input("1.German:English\n2.English:German\n3.Both\n") )
guessed    = []  #guessed.append ( dic_ver.pop(rand_ver) )

dic_ver = load_from_file( open('germ_verb.txt', 'r') )
dic_nom = load_from_file( open('germ_noms.txt', 'r') )

if   (types == 0): dic, Word = dic_ver, Verb     #verb
elif (types == 1): dic, Word = dic_nom, Nom      #nomen

for i in range(turns):
    game_round(dic, Word, transl_dir)
