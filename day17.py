with open("inputs/day17.txt", "r") as file:
    data = file.readlines()

containers = [int(s) for s in data]

n = len(containers)
count = 0
eggnog = 150

minFilled = n + 1
minCount = 0


def backtrace(i, sum, filled):
    global count
    global minCount
    global minFilled

    if i == n:
        if sum == eggnog:
            count += 1
            if filled < minFilled:
                minFilled = filled
                minCount = 1
            elif filled == minFilled:
                minCount += 1
        return

    if sum > eggnog:
        return

    # don't fill it
    backtrace(i + 1, sum, filled)
    # fill it
    backtrace(i + 1, sum + containers[i], filled + 1)


backtrace(0, 0, 0)

print('Part 1', count)
print('Part 2', minCount)
