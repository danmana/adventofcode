with open("inputs/day17.txt", "r") as file:
    data = file.readlines()

containers = [int(s) for s in data]

n = len(containers)
count = 0
eggnog = 150


def backtrace(i, sum):
    global count

    if i == n:
        if sum == eggnog:
            count += 1
        return

    if sum > eggnog:
        return

    backtrace(i + 1, sum)
    backtrace(i + 1, sum + containers[i])


backtrace(0, 0)

print('Part 1', count)
