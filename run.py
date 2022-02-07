from random import randint as rint
from sys import stderr, exit
wordlist = []
GREEN, YELLOW, GRAY = ('0', '1', '2')

def info():
    """
                        Wordle Game Solver
                https://www.powerlanguage.co.uk/wordle/
                 Created by Leo (Lin Yung Hsieh), 2022
                        Any suggestion is welcome!
    Check my code at https://github.com/LeoTheBestCoder/wordle-solver
    """
    return 

def getword():
    # global wordlist
    idx = rint(0, len(wordlist) - 1)
    return wordlist[idx]

def readfile():
    global wordlist
    with open('wordlist.txt', 'r') as fh:
        wordlist = list(map(lambda w: w[:-1] if w[-1] == '\n' else w, fh.readlines()))

def check_r(res: str):
    if len(res) != 5:
        return False
    for ch in res:
        if ch not in ['0', '1', '2']:
            return False
    return True

def update(word: str, res: str):
    global wordlist
    try:
        assert check_r(res)
        for i in range(5):
            invalid = []
            if res[i] == GREEN:
                # correct character + correct position
                for w in wordlist:
                    if w[i] != word[i]:
                        invalid.append(w)
            elif res[i] == YELLOW:
                # correct character + wrong position
                for w in wordlist:
                    if word[i] not in w:
                        invalid.append(w)
                    elif w[i] == word[i]:
                        invalid.append(w)
            elif res[i] == GRAY:
                # wrong character
                for w in wordlist:
                    if word[i] in w:
                        special_case = False
                        for j in range(5):
                            if i != j and word[i] == word[j] and res[j] == GREEN:
                                special_case = True
                        if not special_case:
                            invalid.append(w)
                        else:
                            print(f'{w} is a special case')

            for i_word in invalid:
                wordlist.remove(i_word)
            
    except:
        stderr.write('Invalid input!\n')
        exit(-1)
    


def run():
    print(info.__doc__)
    readfile()
    print("""============================================
If the result is GREEN, enter 0
If the result is YELLOW, enter 1
If the result is GRAY, enter 2
Only a string with length = 5 and contains ONLY 0, 1, 2 is ACCEPTED!
ex. Enter 12200 if the result is "yellow gray gray green green".
============================================\n""")
    _ = input('Ready to start? (Press ENTER to continue)')
    word = getword()
    # print(f'original len = {len(wordlist)}')
    print(f'Try to guess "{word}". What is the result? ', end = '')
    res = input()
    update(word, res)
    # print(f'len = {len(wordlist)}')
    # print(wordlist)
    while res != '00000':
        word = getword()
        print(f'Try to guess "{word}". What is the result? ', end = '')
        res = input()
        update(word, res)
        # print(f'len = {len(wordlist)}')
        # print(wordlist)
    print('Congratulations!')



if __name__ == '__main__':
    run()
    
