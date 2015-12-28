import functools

with open("inputs/day24.txt", "r") as file:
    data = file.readlines()

data = [int(i) for i in data]

n = len(data)
total = sum(data)
w = int(total / 3)


def quantum(x):
    q = 1
    for i in x:
        q *= data[i]
    return q


# brute force will get us nowhere, there are 3^28 possible solutions to consider

# a = [0] * n
# best = None

# def pack(i, s1, s2, s3):
#     global best
#
#     if s1 > w or s2 > w or s3 > w:
#         return
#
#     if i == n:
#         if s1 == s2 and s1 == s3:
#             # solution
#             pack1 = [i for i in range(n) if a[i] == 0]
#             if best == None:
#                 best = pack1
#             elif len(pack1) < len(best):
#                 best = pack1
#             elif len(pack1) == len(best) and quantum(pack1) < quantum(best):
#                 best = pack1
#         return
#
#     a[i] = 0
#     pack(i + 1, s1 + data[i], s2, s3)
#
#     a[i] = 1
#     pack(i + 1, s1, s2 + data[i], s3)
#
#     a[i] = 2
#     pack(i + 1, s1, s2, s3 + data[i])
#
#
# pack(0, 0, 0, 0)
# print("Brute force", quantum(best))



# ok, attempt two:
# try to split the first part, and then just check if the remaining bit can be split

possibilities = []
a = [False] * n
# after running it starting with bestSize n, I found that the bestSize is actually 6
bestSize = 6  # n


def getPossibilities(i, s, size):
    global bestSize
    global possibilities
    global a

    if s > w:
        return

    if size > bestSize:
        return

    if i == n:
        if s == w:
            if size < bestSize:
                possibilities = []
                bestSize = size
            possibilities.append([i for i in range(n) if a[i]])
        return

    if s + data[i] > w:
        # there is no point going on, the numbers are sorted so we won't find anything smaller than this
        return

    a[i] = True
    getPossibilities(i + 1, s + data[i], size + 1)

    a[i] = False
    getPossibilities(i + 1, s, size)


getPossibilities(0, 0, 0)


def cmpSol(a, b):
    cmp = len(a) - len(b)
    if cmp == 0:
        cmp = quantum(a) - quantum(b)
    return cmp


possibilities.sort(key=functools.cmp_to_key(cmpSol))


def canSplit(sol):
    a = [data[i] for i in sol]
    m = len(a)
    K = 2 * w
    maxA = a[-1]

    p = [[False for j in range(m + 1)] for i in range(w + 1)]

    for i in range(m + 1):
        p[0][i] = True

    for i in range(1, w + 1):
        for j in range(1, m + 1):
            p[i][j] = p[i][j - 1] or p[i - a[j - 1]][j - 1]

    return p[w][m]


for sol in possibilities:
    if canSplit(sol):
        print('Quantum 3', quantum(sol))
        break
