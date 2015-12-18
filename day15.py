import re
from collections import namedtuple

with open("inputs/day15.txt", "r") as file:
    data = file.readlines()


class Ingredient(object):
    __line = re.compile(
        '(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')

    def __init__(self, s):
        m = Ingredient.__line.search(s)
        if m == None:
            self.name = None
            self.capacity = 0
            self.durability = 0
            self.flavor = 0
            self.texture = 0
            self.calories = 0
        else:
            self.name = m.group(1)
            self.capacity = int(m.group(2))
            self.durability = int(m.group(3))
            self.flavor = int(m.group(4))
            self.texture = int(m.group(5))
            self.calories = int(m.group(6))


ingredients = [Ingredient(s) for s in data]

n = len(data)
cookie = [None for i in range(n)]

maxScore = 0


def getScore():
    score = Ingredient('')

    for i in range(0, n):
        amount = cookie[i]
        ingredient = ingredients[i]
        score.capacity += amount * ingredient.capacity
        score.durability += amount * ingredient.durability
        score.flavor += amount * ingredient.flavor
        score.texture += amount * ingredient.texture

    return max(0, score.capacity) * max(0, score.durability) * max(0, score.flavor) * max(0, score.texture)


def backtrace(i, volume):
    global maxScore
    global cookie

    if i == n:
        if volume == 100:
            score = getScore()
            if score > maxScore:
                maxScore = score
        return

    for amount in range(0, 100 - volume + 1):
        cookie[i] = amount
        backtrace(i + 1, volume + amount)
        cookie[i] = None


backtrace(0, 0)

print maxScore
