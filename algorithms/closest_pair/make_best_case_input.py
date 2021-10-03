import random
from sys import stderr

print("Give the size of the set of points: ", file=stderr, end="")
size = int(input())

K = 100


def gen_points():
    S = set()

    y = 1

    while len(S) < size:
        x = random.randint(-K, K*size)
        S.add((x, y))
        print(len(S), file=stderr)

    return S


S = gen_points()
for p in S:
    print(f"{p[0]} {p[1]}")
