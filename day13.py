import re

with open("inputs/day13.txt", "r") as file:
    data = file.readlines()

nodes = set()
edges = {}

line = re.compile('(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).')

for s in data:
    m = line.search(s)

    a = m.group(1)
    op = m.group(2)
    val = int(m.group(3))
    if op == 'lose':
        val = -val
    b = m.group(4)

    nodes.add(a)
    nodes.add(b)

    edges[(a, b)] = val


def dist(i, j):
    return edges[(i, j)] + edges[(j, i)]


def backtrace(i, d):
    global path
    global maxDist

    # found a solution
    if i == n:
        d += dist(path[0], path[n - 1])
        if d > maxDist:
            maxDist = d
        return

    for v in nodes:
        if not v in path:
            path[i] = v
            backtrace(i + 1, d + dist(path[i - 1], v))

    path[i] = None


n = len(nodes)
path = [None for i in range(n)]
maxDist = -999999999
for i in nodes:
    path[0] = i
    backtrace(1, 0)

print('Without you', maxDist)

n = len(nodes) + 1
path = [None for i in range(n)]
maxDist = -999999999
for i in nodes:
    edges[('You', i)] = 0
    edges[(i, 'You')] = 0

nodes.add('You')

for i in nodes:
    path[0] = i
    backtrace(1, 0)

print('With you', maxDist)
