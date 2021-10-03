#!/usr/bin/env python3
import matplotlib.pyplot as plt

import argparse
from pathlib import Path


def plot_and_save(all_points, closest_points_pair, plots_file):
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot()

    xs, ys = zip(*all_points)
    plt.plot(xs, ys, 'o', c='k', ms=7, label='all points')

    xs, ys = zip(*closest_points_pair)
    plt.plot(xs, ys, 'o', c='r', ms=10, label='selected points')

    ax.set(
        xlabel='X',
        ylabel='Y',
    )

    plt.grid()
    plt.legend()
    fig.savefig(plots_file)
    plt.show()


def points_from_file(inputs_file):
    points = []
    with inputs_file.open() as f:
        lines = f.readlines()
        points.extend([int(p) for p in line.split()]
                      for line in lines)
    return points


def main():
    parser = argparse.ArgumentParser(
        description='Plots all points from inputs_file and closest pair '
                    'from outputs_file points'
    )
    parser.add_argument(
        'inputs_file',
        type=str,
        help='The file with all the input points'
    )
    parser.add_argument(
        'outputs_file',
        type=str,
        help='The file with the closest points pair'
    )
    parser.add_argument(
        '--plot-file',
        type=str,
        default="plot.jpg",
        help='The file where the plot will be saved'
    )

    args = parser.parse_args()

    inputs_file = Path(args.inputs_file)
    outputs_file = Path(args.outputs_file)
    plots_file = Path(args.plot_file)

    all_points = points_from_file(inputs_file)
    closest_points_pair = points_from_file(outputs_file)

    plot_and_save(all_points, closest_points_pair, plots_file)


if __name__ == '__main__':
    main()
