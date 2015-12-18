from hashlib import md5

secret = "iwrupvqb"


def findIt(s):
    i = 0
    while (True):
        h = md5((secret + repr(i)).encode('utf-8')).hexdigest()
        if h.startswith(s):
            return i
        else:
            i += 1


print("5 zeroes", findIt("00000"))
print("6 zeroes", findIt("000000"))
