from collections import namedtuple

with open("inputs/day23.txt", "r") as file:
    data = file.readlines()

instr = []

Instr = namedtuple('Instr', 'op reg offset')

for s in data:
    if s.startswith('hlf'):
        instr.append(Instr('hlf', s[4], None))
    elif s.startswith('tpl'):
        instr.append(Instr('tpl', s[4], None))
    elif s.startswith('inc'):
        instr.append(Instr('inc', s[4], None))
    elif s.startswith('jmp'):
        instr.append(Instr('jmp', None, int(s[4:])))
    elif s.startswith('jie'):
        instr.append(Instr('jie', s[4], int(s[7:])))
    elif s.startswith('jio'):
        instr.append(Instr('jio', s[4], int(s[7:])))

n = len(instr)

reg = {
    'a': 0,
    'b': 0
}


def runIt():
    i = 0
    while i < n:
        x = instr[i]

        if x.op == 'hlf':
            reg[x.reg] /= 2
        elif x.op == 'tpl':
            reg[x.reg] *= 3
        elif x.op == 'inc':
            reg[x.reg] += 1
        elif x.op == 'jmp':
            i += x.offset
            continue
        elif x.op == 'jie':
            if reg[x.reg] % 2 == 0:
                i += x.offset
                continue
        else:
            if reg[x.reg] == 1:
                i += x.offset
                continue
        i += 1


reg = {
    'a': 0,
    'b': 0
}
runIt()
print('a=0, b=0', reg['b'])

reg = {
    'a': 1,
    'b': 0
}
runIt()
print('a=1, b=0', reg['b'])
