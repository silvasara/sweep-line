#!/usr/bin/env python3
import matplotlib.pyplot as plt
import argparse
from pathlib import Path


def plot_and_save(all_points, plots_file, size):

    size = list(map(float, size.lower().split('x')))
    fig = plt.figure(figsize=size)
    ax = fig.add_subplot()

    (xs0, ys0), *all_points = all_points
    plt.plot(xs0, ys0, 'o', c='k', linestyle="-", label="segmentos")

    for xs, ys in all_points:
        plt.plot(xs, ys, 'o', c='k', linestyle="-")

    ax.set(
        xlabel='X',
        ylabel='Y',
    )

    plt.legend()
    fig.savefig(plots_file)
    plt.show()


def points_from_file(inputs_file):
    points = []
    with inputs_file.open() as f:
        lines = f.readlines()
        intervals = [[int(p) for p in line.split()] for line in lines]
        points.extend([(e[::2], e[1::2]) for e in intervals])

    return points


def main():
    parser = argparse.ArgumentParser(
        description='Plots all points from inputs_file and polygon '
                    'from outputs_file points'
    )
    parser.add_argument(
        'inputs_file',
        type=str,
        help='The file with all the input points'
    )
    parser.add_argument(
        '--plot-file',
        type=str,
        default="plot.jpg",
        help='The file where the plot will be saved'
    )

    parser.add_argument(
        '--size',
        type=str,
        default='5x5',
        help='The size of the image in inches e.g. 5x5'
    )

    args = parser.parse_args()

    inputs_file = Path(args.inputs_file)
    plots_file = Path(args.plot_file)

    all_points = points_from_file(inputs_file)

    plot_and_save(all_points, plots_file, args.size)


if __name__ == '__main__':
    main()
