def play(playersTurn, hp, bossHp, mana, shield, recharge, poison, cost):
    global minMana

    if hardMode and playersTurn:
        hp -= 1

    if hp <= 0:
        return
    if cost >= minMana:
        return

    if poison > 0:
        bossHp -= 3
        poison -= 1

    if bossHp <= 0:
        if cost < minMana:
            minMana = cost
            print("New min", minMana)
        return

    if recharge > 0:
        mana += 101
        recharge -= 1

    trueDmg = 9
    if shield > 0:
        trueDmg -= 7
        shield -= 1

    if playersTurn:
        if recharge == 0 and mana >= 229:
            play(False, hp, bossHp, mana - 229, shield, 5, poison, cost + 229)
        if shield == 0 and mana >= 113:
            play(False, hp, bossHp, mana - 113, 6, recharge, poison, cost + 113)
        if poison == 0 and mana >= 173:
            play(False, hp, bossHp, mana - 173, shield, recharge, 6, cost + 173)
        if mana >= 53:
            play(False, hp, bossHp - 4, mana - 53, shield, recharge, poison, cost + 53)
        if mana >= 73:
            play(False, hp + 2, bossHp - 2, mana - 73, shield, recharge, poison, cost + 73)
        return
    else:
        play(True, hp - trueDmg, bossHp, mana, shield, recharge, poison, cost)


minMana = 99999999
hardMode = False
play(True, 50, 51, 500, 0, 0, 0, 0)
print('Normal', minMana)

minMana = 99999999
hardMode = True
play(True, 50, 51, 500, 0, 0, 0, 0)
print('Hard', minMana)
