import math
from collections import namedtuple
from bisect import bisect_left


Point = namedtuple('Point', 'x y')
Pair = namedtuple('Pair', 'A B')


def get_distance(P, Q):
    return math.hypot(P.x - Q.x, P.y - Q.y)


def get_closest_pair(points):
    N = len(points)
    points.sort()

    distance = get_distance(points[0], points[1])
    closest = Pair(points[0], points[1])

    S = set()

    S.add(Point(points[0].y, points[0].x))
    S.add(Point(points[1].y, points[1].x))

    S = sorted(S)

    for i in range(2, N):
        P = points[i]
        index = bisect_left(S, Point(P.y - distance, 0))
        size_s = len(S)

        while index < size_s:
            set_point = S[index]
            Q = Point(set_point.y, set_point.x)

            if Q.x < P.x - distance:
                index = size_s - 1
                S.remove(set_point)
            if Q.y > P.y + distance:
                break

            curr_distance = get_distance(P, Q)
            if curr_distance < distance:
                distance = curr_distance
                closest = Pair(P, Q)

            index += 1

        S.append(Point(P.y, P.x))

    return closest


points = [
    Point(2, 4),
    Point(5, 3),
    Point(8, 1),
    Point(3, 6),
    Point(1, 1),
    Point(4, 4),
    Point(8, 5),
    Point(6, 2),
    Point(1, 6),
    Point(7, 4),
    Point(8, 6),
    Point(3, 2),
    Point(6, 5),
    Point(-1, 4),
]

closest_pair = get_closest_pair(points)

print(f"A: ({closest_pair.A.x}, {closest_pair.A.y})",
      f"B: ({closest_pair.B.x}, {closest_pair.B.y})")
