import random
import math
import matplotlib.path as mplPath
import numpy as np
from sys import stderr

Ax, Ay = 0, 0
Bx, By = 0, 0
Cx, Cy = 0, 0

K = 100

print("Give the size of the set of points: ", file=stderr, end="")
size = int(input())


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def gen_triangle():
    global Ax, Ay, Bx, By, Cx, Cy

    Ax = random.randint(-K*size, K*size)
    Ay = random.randint(-K*size, K*size)
    Bx = random.randint(-K*size, K*size)
    By = random.randint(-K*size, K*size)
    Cx = random.randint(-K*size, K*size)
    Cy = random.randint(-K*size, K*size)

    a = math.hypot(Ax-Bx, Ay-By)
    b = math.hypot(Bx-Cx, By-Cy)
    c = math.hypot(Cx-Ax, Cy-Ay)

    return a, b, c


def calc_area(a, b, c):
    s = (a + b + c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))  # Heron's formula
    # print("area:", area)
    return area


def gen_points():
    S = set()
    S.add((Ax, Ay))
    S.add((Bx, By))
    S.add((Cx, Cy))

    polygon = mplPath.Path(
        np.array([[Ax, Ay], [Bx, By], [Cx, Cy]])
    )

    while True:
        Px = random.randint(-K*size, K*size)
        Py = random.randint(-K*size, K*size)

        if polygon.contains_point((Px, Py)):
            S.add((Px, Py))
            print(len(S), file=stderr)

        if len(S) >= size:
            break

    return S


a, b, c = gen_triangle()
while not is_triangle(a, b, c) or calc_area(a, b, c) < K*K*size:
    a, b, c = gen_triangle()

# print("sides", a, b, c)
# print("Ponto A:", Ax, Ay)
# print("Ponto B:", Bx, By)
# print("Ponto C:", Cx, Cy)

S = gen_points()
# print("conjunto S")
for p in S:
    print(f"{p[0]} {p[1]}")
