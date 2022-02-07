def alphabet(ch: str) -> bool:
    return True if ord('a') <= ord(ch) <= ord('z') else False

fh = open('/usr/share/dict/words')
fh2 = open('wordlist.txt', 'w')

five = []
for w in fh.readlines():
    new_w = w[:-1] if w[-1] == '\n' else w
    if len(new_w) == 5 and all([alphabet(ch) for ch in new_w]):
        five.append(new_w)
        fh2.write(new_w + '\n')
fh.close()
fh2.close()
