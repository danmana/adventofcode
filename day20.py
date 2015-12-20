import math


def getDivs(n):
    divs = []
    maxi = int(math.sqrt(n))
    for i in range(1, maxi + 1):
        if n % i == 0:
            divs.append(i)
            j = int(n / i)
            if i < j:
                divs.append(j)

    return divs


n = 29000000
i = 665000
sol1 = None
sol2 = None
while sol1 is None or sol2 is None:
    divs = getDivs(i)

    if sol1 is None:
        presents = sum(divs) * 10
        if presents >= n:
            sol1 = i
            print('Infinite', sol1)

    if sol2 is None:
        divs50 = [x for x in divs if i / x <= 50]
        presents50 = sum(divs50) * 11
        if presents50 >= n:
            sol2 = i
            print('Only 50', sol2)
    i += 1
