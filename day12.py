import json

with open("inputs/day12.txt", "r") as file:
    data = file.read()

obj = json.loads(data)

n = 0


def process(obj):
    global n

    if isinstance(obj, int):
        n += obj
    elif isinstance(obj, list):
        for x in obj:
            process(x)
    elif isinstance(obj, dict):
        for x in obj:
            process(obj[x])

process(obj)

print n