import random
from sys import stderr

Ax, Ay = 0, 0

K = 100

print("Give the size of the set of points: ", file=stderr, end="")
size = int(input())


def gen_points():
    S = set()
    S.add((Ax, Ay))

    while True:
        Px = random.randint(-K*size, K*size)
        Py = random.randint(-K*size, K*size)
        S.add((Px, Py))

        print(len(S), file=stderr)

        if len(S) >= size:
            break

    return S


S = gen_points()
for p in S:
    print(f"{p[0]} {p[1]}")
