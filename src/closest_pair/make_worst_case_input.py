import random
from sys import stderr

K = 100

print("Give the size of the set of points: ", file=stderr, end="")
size = int(input())
size_lines = size/2


def gen_points():
    S = set()

    x_1 = 1
    y_1 = 1

    x_2 = random.randint(x_1+2, K)

    S.add((x_1, y_1))
    S.add((x_2, y_1))

    while len(S) < size:
        y = random.randint(y_1, K*size)
        S.add((x_1, y))
        S.add((x_2, y))

        print(len(S), file=stderr)

    return S


S = gen_points()
for p in S:
    print(f"{p[0]} {p[1]}")
