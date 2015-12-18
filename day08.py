import re

with open("inputs/day08.txt", "r") as file:
    data = file.readlines()

n = 0


for s in data:
    s2 = re.sub(r'\\\\|\\"|\\x..', '!', s)
    print s2
    n += len(s) - len(s2) + 2


print n;
