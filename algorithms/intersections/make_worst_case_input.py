import random
from sys import stderr
from collections import namedtuple

K = 100
Point = namedtuple('Point', 'x y')
Interval = namedtuple('Interval', 'A B')

print("Give the size of the set of points: ", file=stderr, end="")
size = int(input())


def gen_lines():
    intervals = []

    length = random.randint(K/2, K)

    h_x_a = random.randint(1, K)
    h_x_b = h_x_a + length

    v_y_a = random.randint(1, K)
    v_y_b = v_y_a + length

    for i in range(size):
        if i % 2:  # verticals
            x_a = random.randint(h_x_a, h_x_b)
            x_b = x_a

            A = Point(x_a, v_y_a)
            B = Point(x_b, v_y_b)
        else:  # horizontals
            y_a = random.randint(v_y_a, v_y_b)
            y_b = y_a

            A = Point(h_x_a, y_a)
            B = Point(h_x_b, y_b)

        intervals.append(Interval(A, B))

        print(len(intervals), file=stderr)
    return intervals


intervals = gen_lines()
for i in intervals:
    print(f"{i.A.x} {i.A.y} {i.B.x} {i.B.y}")
