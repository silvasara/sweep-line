from collections import namedtuple
import sys


def get_determinant(P, A, B):
    return (P.x * A.y + P.y * B.x + A.x * B.y) -\
           (B.x * A.y + B.y * P.x + A.x * P.y)


def make_hull(P):
    hull = []

    for p in P:
        size = len(hull)

        while size >= 2 and get_determinant(
                hull[size-2], hull[size-1], p) <= 0:
            hull.pop()
            size = len(hull)

        hull.append(p)

    return hull


def make_monotone_chain(P):
    P.sort()

    lower_hull, upper_hull = [], []

    lower_hull = make_hull(P)

    P.reverse()

    upper_hull = make_hull(P)

    if lower_hull:
        lower_hull.pop()
    lower_hull.extend(upper_hull)

    return lower_hull


Point = namedtuple('Point', 'x y')

P = []

for line in sys.stdin:
    x, y = map(int, line.split())
    P.append(Point(x, y))

ch = make_monotone_chain(P)
i = 0
for i in range(len(ch)):
    print(f"{ch[i].x} {ch[i].y}")
