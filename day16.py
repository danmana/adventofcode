import json

with open("inputs/day16.txt", "r") as file:
    data = file.readlines()


def parseSue(s):
    s = s[s.index(':') + 2:]
    s = s.replace(':', '":')
    s = s.replace(', ', ', "')

    return json.loads('{"' + s + '}')


clue = parseSue('Clue : children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1')


def isSue(sue):
    for prop in sue:
        if (not prop in clue) or sue[prop] != clue[prop]:
            return False
    return True


def isRealSue(sue):
    for prop in sue:
        if not prop in clue:
            print(prop)
            return False
        if prop == 'cats' or prop == 'trees':
            if sue[prop] <= clue[prop]:
                return False
        elif prop == 'pomeranians' or prop == 'goldfish':
            if sue[prop] >= clue[prop]:
                return False
        elif sue[prop] != clue[prop]:
            return False
    return True


for i in range(500):
    sue = parseSue(data[i])
    if isSue(sue):
        print('Sue', i + 1)
    if isRealSue(sue):
        print('Real Sue', i + 1)
