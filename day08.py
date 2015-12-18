import re

with open("inputs/day08.txt", "r") as file:
    data = file.readlines()

n = 0
n2 = 0

for s in data:
    s1 = re.sub(r'\\\\|\\"|\\x..', '!', s)
    s2 = re.sub(r'"|\\', '!!', s)
    n += len(s) - len(s1) + 2
    n2 += len(s2) - len(s) + 2

print('Part 1', n)
print('Part 2', n2)
