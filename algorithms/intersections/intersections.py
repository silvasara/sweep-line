import sys
from bisect import bisect_left
from collections import namedtuple
import time


class BITree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 1)

    def get_LSB(self, n):
        return n & -n

    def get_RSQ(self, i):
        sum_ = 0

        while i >= 1:
            sum_ += self.tree[i]
            i -= self.get_LSB(i)

        return sum_

    def add(self, i, x):
        if i == 0:
            return

        while i <= self.size:
            self.tree[i] += x
            i += self.get_LSB(i)


def get_index(heights, value):
    index = bisect_left(heights, value)

    return index + 1  # count start 1


def count_intersections(intervals):
    events = []
    heights = set()

    for i in intervals:
        heights.update([i.A.y, i.B.y])

        x_min = min(i.A.x, i.B.x)
        x_max = max(i.A.x, i.B.x)

        index = intervals.index(i)

        if i.A.x == i.B.x:  # vertical
            events.append((x_min, 2, index))
        else:  # horizontal
            events.append((x_min, 1, index))
            events.append((x_max, 3, index))

    events.sort()
    heights = sorted(heights)
    fenwick_tree = BITree(len(heights))
    total = 0

    for e in events:
        _, type_, idx = e
        i = intervals[idx]

        if type_ == 1:  # event type 1
            y = get_index(heights, i.A.y)
            fenwick_tree.add(y, 1)
        elif type_ == 2:  # event type 2
            y_min = min(get_index(heights, i.A.y), get_index(heights, i.B.y))
            y_max = max(get_index(heights, i.A.y), get_index(heights, i.B.y))
            total += fenwick_tree.get_RSQ(y_max) -\
                fenwick_tree.get_RSQ(y_min-1)
        else:  # event type 3
            y = get_index(heights, i.B.y)
            fenwick_tree.add(y, -1)

    return total


Point = namedtuple('Point', 'x y')
Interval = namedtuple('Interval', 'A B')

intervals = []

for line in sys.stdin:
    x_a, y_a, x_b, y_b = map(int, line.split())
    A = Point(x_a, y_a)
    B = Point(x_b, y_b)
    intervals.append(Interval(A, B))

begin = time.perf_counter()

answer = count_intersections(intervals)

end = time.perf_counter()
elapsed = (end - begin)

print(f"Time measured: {round(elapsed, 6)} seconds.", file=sys.stderr)

print(answer)
