# Самая далекая планета
from math import pi

def find_farthest_orbit(list_of_orbits):
    return max(list(map(lambda x, y:  pi*x*y, list_of_orbits), ))



orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))