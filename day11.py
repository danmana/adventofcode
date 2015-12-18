import re




def rule1(s):
    for i in range(0, len(s)-2):
        if ord(s[i]) == ord(s[i+1]) -1 and ord(s[i]) == ord(s[i+2]) - 2:
            return True
    return False

invalid = re.compile('[ilo]')
def rule2(s):
    return invalid.search(s) is None

pair = re.compile(r'(\w)\1')
def rule3(s):
    m = pair.search(s)
    if m is not None:
        m = pair.search(s,m.end())
        return m is not None
    return False

def isValid(s):
    return rule1(s) and rule2(s) and rule3(s)

def nextPass(s):
    s = list(s)
    n = len(s)
    maxCh = ord('z')
    for i in reversed(range(n)):
        ch = s[i]
        nextCh = ord(ch) + 1
        if nextCh > maxCh:
            s[i] = 'a'
        else:
            s[i] = chr(nextCh)
            break
    return ''.join(s)


password = "cqjxjnds"
while True:
    password = nextPass(password)
    if isValid(password):
        print password
        break