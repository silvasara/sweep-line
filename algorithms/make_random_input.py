import random
import math
import matplotlib.path as mplPath
import numpy as np
from sys import stderr

Ax, Ay = 0, 0

K = 100

print("Give the size of the set of points: ", file=stderr, end="")
size = int(input())


def gen_polygon():
    global Ax, Ay

    Ax = random.randint(-K*size, K*size)
    Ay = random.randint(-K*size, K*size)
    
    radius = random.randint(K, K*size)

    return radius


def calc_area(radius):
    return math.pi * radius**2


def gen_points():
    S = set()
    S.add((Ax, Ay))

    while True:
        Px = random.randint(Ax-radius, Ax+radius)
        Py = random.randint(Ay-radius, Ay+radius)

        if math.hypot(Px - Ax, Py - Ay) < radius:
            S.add((Px, Py))
            print(len(S), file=stderr)

        if len(S) >= size:
            break

    return S


radius = gen_polygon()
while not calc_area(radius) < K*K*size:
    radius = gen_polygon()

# print("sides", a, b, c)
# print("Ponto A:", Ax, Ay)
# print("Ponto B:", Bx, By)
# print("Ponto C:", Cx, Cy)

S = gen_points()
# print("conjunto S")
for p in S:
    print(f"{p[0]} {p[1]}")
