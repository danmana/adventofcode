import re

with open("inputs/day05.txt", "r") as file:
    data = file.readlines()

vowels = re.compile('[aeiou]', re.IGNORECASE)
dupes = re.compile(r'(\w)\1')
invalid = re.compile('ab|cd|pq|xy')
dupes2 = re.compile(r'(\w\w).*\1')
repeats = re.compile(r'(\w).\1')


def isNice(s):
    if len(vowels.findall(s)) < 3:
        return False
    if dupes.search(s) == None:
        return False
    if invalid.search(s) != None:
        return False
    return True


def isNice2(s):
    if dupes2.search(s) == None:
        return False
    if repeats.search(s) == None:
        return False
    return True


nice = 0
nice2 = 0

for s in data:
    if isNice(s):
        nice += 1
    if isNice2(s):
        nice2 += 1

print('Nice 1', nice)
print('Nice 2', nice2)
