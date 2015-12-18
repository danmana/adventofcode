import re

with open("inputs/day07.txt", "r") as file:
    data = file.readlines()

wires = {}

instr = re.compile('^(.+) -> (\w+)$',re.IGNORECASE)

number = re.compile('^(\d+)$',re.IGNORECASE)
assign = re.compile('^(\w+)$',re.IGNORECASE)
notOp = re.compile('^NOT (\w+)$',re.IGNORECASE)
multiOp = re.compile('^(\w+) (\w+) (\w+)$',re.IGNORECASE)

def preProcessLine(s):
    m = instr.search(s)
    wires[m.group(2)] = m.group(1)

for s in data:
    preProcessLine(s)


def getVal(w):
    m = number.search(w)
    if m != None:
        return int(m.group(1))

    exp = wires[w]

    if isinstance(exp, int):
        return exp

    m = assign.search(exp)
    if m != None:
        a = m.group(1)
        val = getVal(a)
        wires[a] = val
        return val

    m = notOp.search(exp)
    if m != None:
        a = m.group(1)
        val = ~ getVal(a)
        wires[a] = val
        return val

    m = multiOp.search(exp)
    if m != None:
        op = m.group(2)
        a = m.group(1)
        b = m.group(3)
        if op == 'AND':
            val = getVal(a) & getVal(b)
        elif op == 'OR':
            val = getVal(a) | getVal(b)
        elif op == 'LSHIFT':
            val = getVal(a) << getVal(b)
        elif op == 'RSHIFT':
            val = getVal(a) >> getVal(b)
        elif op == 'XOR':
            val = getVal(a) ^ getVal(b)

        wires[w] = val
        return val



print getVal('a');
