from collections import namedtuple

Item = namedtuple('Item', 'name cost damage armor')

weapons = [
    Item('Dagger', 8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer', 25, 6, 0),
    Item('Longsword', 40, 7, 0),
    Item('Greataxe', 74, 8, 0)
]

armor = [
    None,
    Item('Leather', 13, 0, 1),
    Item('Chainmail', 31, 0, 2),
    Item('Splintmail', 53, 0, 3),
    Item('Bandedmail', 75, 0, 4),
    Item('Platemail', 102, 0, 5)
]

rings = [
    None,
    Item('Damage +1', 25, 1, 0),
    Item('Damage +2', 50, 2, 0),
    Item('Damage +3', 100, 3, 0),
    Item('Defense +1', 20, 0, 1),
    Item('Defense +2', 40, 0, 2),
    Item('Defense +3', 80, 0, 3)
]

Human = namedtuple('Human', 'life damage armor')

boss = Human(104, 8, 1)


def isWinner(player):
    playerDmg = max(1, player.damage - boss.armor)
    bossDmg = max(1, boss.damage - player.armor)

    playerRounds = int(boss.life / playerDmg)
    if boss.life % playerDmg != 0:
        playerRounds += 1

    bossRounds = int(player.life / bossDmg)
    if player.life % bossDmg != 0:
        bossRounds += 1

    return playerRounds <= bossRounds


minCost = 99999999
maxCost = 0

for w in weapons:
    for a in armor:
        for r1 in rings:
            for r2 in rings:
                cost = w.cost
                dmg = w.damage
                arm = 0
                if a is not None:
                    cost += a.cost
                    arm += a.armor
                if r1 is not None:
                    cost += r1.cost
                    dmg += r1.damage
                    arm += r1.armor
                if r2 is not None and r1 != r2:
                    cost += r2.cost
                    dmg += r2.damage
                    arm += r2.armor
                if isWinner(Human(100, dmg, arm)):
                    minCost = min(minCost, cost)
                else:
                    maxCost = max(maxCost, cost)

print('Min to win', minCost)
print('Max to lose', maxCost)
