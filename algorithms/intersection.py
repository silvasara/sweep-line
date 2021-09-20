from bisect import bisect_left
from collections import namedtuple


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

    return index + 1  # contagem inicia em 1


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

        if type_ == 1:  # evento tipo 1
            y = get_index(heights, i.A.y)
            fenwick_tree.add(y, 1)
        elif type_ == 2:  # evento tipo 2
            y_min = min(get_index(heights, i.A.y), get_index(heights, i.B.y))
            y_max = max(get_index(heights, i.A.y), get_index(heights, i.B.y))
            total += fenwick_tree.get_RSQ(y_max) - fenwick_tree.get_RSQ(y_min)
        else:  # evento tipo 3
            y = get_index(heights, i.B.y)
            fenwick_tree.add(y, -1)

    return total


Point = namedtuple('Point', 'x y')
Interval = namedtuple('Interval', 'A B')


intervals = [
    Interval(Point(2, 6), Point(5, 6)),
    Interval(Point(1, 5), Point(6, 5)),
    Interval(Point(5, 4), Point(8, 4)),
    Interval(Point(3, 3), Point(7, 3)),
    Interval(Point(5, 2), Point(8, 2)),
    Interval(Point(1, 1), Point(4, 1)),
    Interval(Point(4, 7), Point(4, 2)),
    Interval(Point(2, 3), Point(2, 0)),
    Interval(Point(6, 3), Point(6, 1)),
]

answer = count_intersections(intervals)

print(answer)
