with open("inputs/day01.txt", "r") as file:
    data = file.read()
level = 0
basement = None
for i in range(len(data)):
    c = data[i]
    if (c == '('):
        level += 1
    elif (c == ')'):
        level -= 1

    if basement is None and level == -1:
        basement = i + 1

print 'Level', level
print 'Basement', basement
