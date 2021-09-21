import random
import math
import matplotlib.path as mplPath
import numpy as np
from sys import stderr

Ax, Ay = 0, 0
Bx, By = 0, 0
Cx, Cy = 0, 0
Dx, Dy = 0, 0

K = 100

print("Give the size of the set of points: ", file=stderr, end="")
size = int(input())


def gen_rectangle():
    global Ax, Ay, Bx, By, Cx, Cy, Dx, Dy

    Ax = random.randint(-K*size, K*size)
    Ay = random.randint(-K*size, K*size)

    h = random.randint(1, K*size)
    w = random.randint(1, K*size)

    Bx = Ax + w
    By = Ay

    Cx = Bx
    Cy = By - h
    
    Dx = Cx - w 
    Dy = Cy

    return h, w


def calc_area(h, w):
    return h * w


def gen_points():
    S = set()
    S.add((Ax, Ay))
    S.add((Bx, By))
    S.add((Cx, Cy))
    S.add((Dx, Dy))

    while True:
        Px = random.randint(Ax, Bx)
        Py = random.randint(Dy, Ay)

        S.add((Px, Py))
       # if polygon.contains_point((Px, Py)):
       #     S.add((Px, Py))
       #     print(len(S), file=stderr)

        if len(S) >= size:
            break

    return S


h, w = gen_rectangle()
while not calc_area(h, w) < K*K*size:
    h, w = gen_rectangle()

# print("sides", a, b, c)
# print("Ponto A:", Ax, Ay)
# print("Ponto B:", Bx, By)
# print("Ponto C:", Cx, Cy)

S = gen_points()
# print("conjunto S")
for p in S:
    print(f"{p[0]} {p[1]}")
