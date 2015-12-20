import re

with open("inputs/day19.txt", "r") as file:
    data = file.readlines()

replacements = {}
reverseReplacements = {}

replacement = re.compile('(\w+) => (\w+)')

for s in data:
    m = replacement.search(s)
    if m is not None:
        a = m.group(1)
        b = m.group(2)
        if a in replacements:
            replacements[a].append(b)
        else:
            replacements[a] = [b]
        if b in reverseReplacements:
            reverseReplacements[b].append(a)
        else:
            reverseReplacements[b] = [a]
    else:
        if len(s):
            medicine = s.strip()

sources = '(' + '|'.join(replacements.keys()) + ')'
sources = re.compile(sources)


def nextMolecules(s):
    posibilities = set()

    matches = sources.finditer(s)

    for m in matches:
        a = m.group(1)
        start, end = m.span(1)
        for b in replacements[a]:
            posibilities.add(s[0:start] + b + s[end:])

    return posibilities


print('Calibration', len(nextMolecules(medicine)))


# brute forcing it is too slow, need to find a better way

# brute force forward
# def findShortest():
#     visited = ['e']
#     steps = [0]
#     i = 0
#
#     while i < len(visited):
#         molecule = visited[i]
#         step = steps[i]
#
#         if i % 1000 == 0:
#             print('At', i, '/', len(visited), ':', step, molecule)
#
#         if molecule == medicine:
#             return step
#
#         nextMols = nextMolecules(molecule)
#
#         for mol in nextMols:
#             if mol not in visited:
#                 visited.append(mol)
#                 steps.append(step + 1)
#
#         i += 1
#
#     return None
#
#
#
# print('Production', findShortest())


# brute force backwards
# targets = reverseReplacements.keys()
#
# visited = set()
#
#
# def findPossibleSources(s):
#     possible = set()
#
#     if s in visited:
#         return possible
#     visited.add(s)
#
#     for t in targets:
#         rt = re.compile(t)
#         matches = rt.finditer(s)
#         if matches is not None:
#             sources = reverseReplacements[t]
#             for m in matches:
#                 start, end = m.span(0)
#                 for source in sources:
#                     possibleSource = s[0:start] + source + s[end:]
#                     if possibleSource not in visited:
#                         possible.add(possibleSource)
#
#     return possible
#
#
# def findMinSteps(s):
#     if s == 'e':
#         return 0
#
#     sources = findPossibleSources(s)
#     steps = []
#
#     for source in sources:
#         minStep = findMinSteps(source)
#         if minStep is not None:
#             steps.append(minStep)
#
#     if len(steps) == 0:
#         return None
#     else:
#         return min(steps)

# print('Production', findMinSteps(medicine))
