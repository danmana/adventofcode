import json

with open("inputs/day12.txt", "r") as file:
    data = file.read()

obj = json.loads(data)


def isRed(obj):
    for x in obj:
        if obj[x] == 'red':
            return True
    return False


def process(obj, excludeRed):
    n = 0

    if isinstance(obj, int):
        n += obj
    elif isinstance(obj, list):
        for x in obj:
            n += process(x, excludeRed)
    elif isinstance(obj, dict):
        if not excludeRed or not isRed(obj):
            for x in obj:
                n += process(obj[x], excludeRed)
    return n


print('All', process(obj, False))
print('Excluding red', process(obj, True))
