import re

with open("inputs/day06.txt", "r") as file:
    data = file.readlines()

pattern = re.compile('(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', re.IGNORECASE)


def processLine(s):
    m = pattern.search(s)
    if m != None:
        action = m.group(1)
        start = (int(m.group(2)), int(m.group(3)))
        end = (int(m.group(4)), int(m.group(5)))
        if action == "turn on":
            turn(start, end, 1)
        elif action == "turn off":
            turn(start, end, -1)
        else:
            if mode == 'part1':
                toggle(start, end)
            else:
                turn(start, end, 2)


def turn(start, end, val):
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if mode == 'part1':
                lights[i][j] = 1 if val > 0 else 0
            else:
                lights[i][j] = max(lights[i][j] + val, 0)


def toggle(start, end):
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            lights[i][j] = 0 if lights[i][j] > 0 else 1


def count():
    on = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            on += lights[i][j]
    return on


mode = 'part1'
lights = [[0 for i in range(0, 1000)] for j in range(0, 1000)]

for s in data:
    processLine(s)

print('Part 1', count())

mode = 'part2'
lights = [[0 for i in range(0, 1000)] for j in range(0, 1000)]

for s in data:
    processLine(s)

print('Part 2', count())
