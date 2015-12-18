import re

s = "1113222113"

def lookAndSay(s):
    s2 = ""
    n = 1
    ch = s[0]
    for i in range(1,len(s)):
        if s[i] == ch:
            n += 1
        else:
            s2 += str(n) + ch
            ch = s[i]
            n = 1
    s2 += str(n) + ch
    return s2

for i in range(0,40):
    s = lookAndSay(s);

print len(s)
