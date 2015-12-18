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
    edges[(a,b)] = edges[(b,a)] =int(m.group(3))

n = len(nodes)
path = [None for i in range(0,n)]
minDist = 999999999


def backtrace(i, d):
    global path
    global minDist

    # there is no point in going on this path any further, we already exceeded the best so far
    if d > minDist:
        return

    # found a solution
    if i == n:
        minDist = d
        return

    for v in nodes:
        e = (path[i-1],v)
        if (not v in path) and e in edges:
            path[i] = v
            backtrace(i+1, d + edges[e])

    path[i] = None


for i in nodes:
    path[0] = i
    backtrace(1, 0)

print minDist









# dist = {}
# def floydWarshall():
#     for i in nodes:
#         for j in nodes:
#             if i == j:
#                 dist[(i,j)] = 0
#             elif (i,j) in edges:
#                 dist[(i,j)] = edges[(i,j)]
#             else:
#                 dist[(i,j)] = 9999999;
#     for k in nodes:
#         for i in nodes:
#             for j in nodes:
#                 d = dist[(i,k)] + dist[(k,j)]
#                 if dist[(i,j)] > d:
#                     dist[(i,j)] = d
#
# floydWarshall()
#
# min = dist.keys()[0]
#
# for (i,j) in dist:
#     if i != j and dist[(i,j)] < dist[min]:
#         min = (i,j)
# print dist[min];
