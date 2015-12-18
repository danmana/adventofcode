with open("inputs/day03.txt", "r") as file:
    data = file.read()

houses = set()
i = 0;
j = 0;

def nextStep(pos, c):
    if c == '>':
        return (pos[0] + 1, pos[1])
    if c == '<':
        return (pos[0] - 1, pos[1])
    if c == '^':
        return (pos[0], pos[1] + 1)
    if c == 'v':
        return (pos[0], pos[1] - 1)

santa = (i,j)
houses.add(santa)
for c in data:
    santa = nextStep(santa, c)
    houses.add(santa)

print 'Santa', len(houses)



houses = set()
santa = (0,0)
robo = (0,0)

houses.add(santa)

santasTurn = True

for c in data:

    if santasTurn:
        santa = nextStep(santa, c)
        houses.add(santa)
    else:
        robo = nextStep(robo, c)
        houses.add(robo)
    santasTurn = not santasTurn

print 'Santa + Robo', len(houses)

