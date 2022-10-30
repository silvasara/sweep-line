import random
from sys import stderr

Ax, Ay = 0, 0
Bx, By = 0, 0
Cx, Cy = 0, 0
Dx, Dy = 0, 0

K = 1000

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

    while len(S) < size:
        Px = random.randint(Ax, Bx)
        Py = Ay
        S.add((Px, Py))  # side A-B

        if len(S) < size:
            Px = Bx
            Py = random.randint(Cy, By)
            S.add((Px, Py))  # side C-B

        if len(S) < size:
            Px = random.randint(Dx, Cx)
            Py = Dy
            S.add((Px, Py))  # side D-C

        if len(S) < size:
            Px = Ax
            Py = random.randint(Dy, Ay)
            S.add((Px, Py))  # side D-A

        print(len(S), file=stderr)

    return S


h, w = gen_rectangle()
ratio = min(h, w)/max(h, w)
while calc_area(h, w) < K*K*size or ratio < 0.25:
    h, w = gen_rectangle()
    ratio = min(h, w)/max(h, w)

S = gen_points()
for p in S:
    print(f"{p[0]} {p[1]}")
