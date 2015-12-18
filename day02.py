with open("inputs/day02.txt", "r") as file:
    data = file.readlines()

paper = 0
ribbon = 0


def calculateWrappingSize(s):
    global paper
    global ribbon

    sizes = [int(x) for x in s.split("x")]
    sizes = sorted(sizes)

    paper += 2 * sizes[0] * sizes[1] + 2 * sizes[0] * sizes[2] + 2 * sizes[1] * sizes[2] + sizes[0] * sizes[1]
    ribbon += 2 * sizes[0] + 2 * sizes[1] + sizes[0] * sizes[1] * sizes[2]


for s in data:
    calculateWrappingSize(s)

print 'Paper', paper
print 'Ribbon', ribbon
