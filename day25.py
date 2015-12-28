import re

with open("inputs/day25.txt", "r") as file:
    data = file.read()

m = re.compile('row (\d+), column (\d+)').search(data)

row = int(m.group(1))
col = int(m.group(2))


def getN(row, col):
    diag = row + col - 1

    n = int(diag * (diag + 1) / 2) - row + 1
    return n


n = getN(row, col)
print('N', n)

code = 20151125

for i in range(1, n):
    code = (code * 252533) % 33554393

print('Code', code)
