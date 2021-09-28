import random
from sys import stderr

K = 1000

print("Give the size of the set of points: ", file=stderr, end="")
size = int(input())
size_lines = size/2


def gen_points():
    S = set()

    x_1 = 1
    x_2 = random.randint(x_1, K)

    i = 0
    while len(S) < size:
        y = random.randint(1, size)

        if i % 2:
            S.add((x_1, y))
        else:
            S.add((x_2, y))

        i += 1

        print(len(S), file=stderr)

    return S


S = gen_points()
for p in S:
    print(f"{p[0]} {p[1]}")
