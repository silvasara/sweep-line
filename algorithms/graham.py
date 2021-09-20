import math
from functools import cmp_to_key
from collections import namedtuple


P0 = ()


def get_distance(get_pivot, point):
    return math.hypot(point.x - get_pivot.x, point.y - get_pivot.y)


def get_determinant(P, A, B):
    return (P.x * A.y + P.y * B.x + A.x * B.y) -\
           (B.x * A.y + B.y * P.x + A.x * P.y)


def get_pivot(P):
    i = 0
    while i < len(P):
        if P[i].y < P[0].y or (P[i].y == P[0].y and P[i].x > P[0].x):
            P[i], P[0] = P[0], P[i]
        i += 1
    return P[0]


def sort_by_angle(A, B):
    # pontos colineares: escolhe-se o mais próximo do pivô
    # se o get_determinante for 0, os pontos estão alinhados
    if get_determinant(P0, A, B) == 0:
        if get_distance(P0, A) < get_distance(P0, B):
            return -1
        if get_distance(P0, A) > get_distance(P0, B):
            return 1
        return 0

    alfa = math.atan((A.y - P0.y)/(A.x - P0.x))
    beta = math.atan((B.y - P0.y)/(B.x - P0.x))

    if alfa < beta:
        return -1
    if alfa > beta:
        return 1
    return 0


def make_convex_hull(P):
    N = len(P)

    # Corner case: com 3 vértices ou menos, P é o próprio convex hull
    if N <= 3:
        return P

    global P0
    P0 = get_pivot(P)
    P.remove(P0)

    P.sort(key=cmp_to_key(sort_by_angle))

    N = len(P)

    # o primeiro ponto é igual ao último
    ch = [P[N-1], P0, P[0]]

    i = 1
    while i < N:
        j = len(ch) - 1

        # se o get_determinante for positivo, a orientação de manteve
        if get_determinant(ch[j-1], ch[j], P[i]) > 0:
            ch.append(P[i])
            i += 1
        else:
            ch.pop()

    return ch


Point = namedtuple('Point', 'x y')

P = [
    Point(0, 0),
    Point(5, 3),
    Point(8, -2),
    Point(4, 4),
    Point(2, 1),
    Point(2, 5),
    Point(3, -1),
    Point(7, 2),
    Point(5, 0),
    Point(0, 4),
    Point(1, -1),
    Point(7, -2),
    Point(6, 4),
    Point(6, 0),
    Point(1, 3)
]

ch = make_convex_hull(P)
i = 0
for i in range(len(ch)):
    print(f"{i+1}: ({ch[i].x}, {ch[i].y})")
