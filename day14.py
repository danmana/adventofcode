import re
from collections import namedtuple

with open("inputs/day14.txt", "r") as file:
    data = file.readlines()

line = re.compile('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')

time = 2503

Raindeer = namedtuple('Raineer', 'name distance')

max = Raindeer(None, 0)

for s in data:
    m = line.search(s)
    name = m.group(1)
    speed = int(m.group(2))
    stamina = int(m.group(3))
    rest = int(m.group(4))

    period = stamina + rest

    distance = int(time / period) * speed * stamina + min(stamina, (time % period)) * speed

    if (distance > max.distance):
        max = Raindeer(name,distance)

print max



