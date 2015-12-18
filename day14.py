import re
from collections import namedtuple

with open("inputs/day14.txt", "r") as file:
    data = file.readlines()

line = re.compile('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')

time = 2503

Raindeer = namedtuple('Raineer', 'name speed stamina rest period distance')

raindeer = []

for s in data:
    m = line.search(s)
    name = m.group(1)
    speed = int(m.group(2))
    stamina = int(m.group(3))
    rest = int(m.group(4))

    period = stamina + rest

    distance = int(time / period) * speed * stamina + min(stamina, (time % period)) * speed

    raindeer.append(Raindeer(name, speed, stamina, rest, period, distance))

raindeer = sorted(raindeer, key=lambda r: r.distance, reverse=True)

print('By Distance', raindeer[0].distance)

n = len(raindeer)
dist = [0] * n
scores = [0] * n

for t in range(2503):
    maxDist = 0
    for i in range(n):
        r = raindeer[i]
        if t % r.period < r.stamina:
            dist[i] += r.speed
        if dist[i] > maxDist:
            maxDist = dist[i]
    for i in range(n):
        if dist[i] == maxDist:
            scores[i] += 1

print('By score', sorted(scores, reverse=True)[0])
