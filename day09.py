import re

with open("inputs/day09.txt", "r") as file:
    data = file.readlines()

nodes = set()
edges = {}

regex = re.compile('(\w+) to (\w+) = (\d+)')

for s in data:
    m = regex.search(s)
    a = m.group(1)
    b = m.group(2)
    nodes.add(a)
    nodes.add(b)
    edges[(a, b)] = edges[(b, a)] = int(m.group(3))

n = len(nodes)
path = [None for i in range(0, n)]
minDist = 999999999
maxDist = 0


def backtrace(i, d):
    global path
    global minDist
    global maxDist

    # found a solution
    if i == n:
        minDist = min(d, minDist)
        maxDist = max(d, maxDist)
        return

    for v in nodes:
        e = (path[i - 1], v)
        if (not v in path) and e in edges:
            path[i] = v
            backtrace(i + 1, d + edges[e])

    path[i] = None


for i in nodes:
    path[0] = i
    backtrace(1, 0)

print('Min', minDist)
print('Max', maxDist)
