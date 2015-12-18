import re

with open("inputs/day06.txt", "r") as file:
    data = file.readlines()

lights = [[False for i in range(0,1000)] for j in range(0,1000)]

pattern = re.compile('(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)',re.IGNORECASE)

def processLine(s):
    m = pattern.search(s)
    if m != None:
        action = m.group(1)
        start = (int(m.group(2)), int(m.group(3)))
        end = (int(m.group(4)), int(m.group(5)))
        if action == "turn on":
            turn(start,end,True)
        elif action == "turn off":
            turn(start,end,False)
        else:
            toggle(start,end)

def turn(start, end, val):
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            lights[i][j] = val

def toggle(start, end):
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            lights[i][j] = not lights[i][j]


for s in data:
    processLine(s)


on = 0
for i in range(0,1000):
    for j in range(0,1000):
        if lights[i][j]:
            on +=1

print on
