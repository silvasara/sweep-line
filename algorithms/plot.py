#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.path as path
import matplotlib.patches as patches
import numpy as np

import argparse
from pathlib import Path


def plot_and_save(all_points, polygon_points, plots_file):
    polygon_points.append(polygon_points[-1])
    polygon = path.Path(np.array(polygon_points), closed=True)

    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot()

    patch = patches.PathPatch(polygon, facecolor='lightgreen', lw=2, label='selected polygon')
    ax.add_patch(patch)

    xs, ys = zip(*polygon_points)
    plt.plot(xs, ys, 'o', c='k', ms=10, label='selected points')

    xs, ys = zip(*all_points)
    plt.plot(xs, ys, 'o', c='r', ms=3, label='all points')

    ax.set(
        xlabel='X',
        ylabel='Y',
        aspect='equal'
    )

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
        description='Plots all points from inputs_file and polygon from outputs_file points'
    )
    parser.add_argument('inputs_file',
        type=str,
        help='The file with all the input points'
    )
    parser.add_argument(
        'outputs_file',
        type=str,
        help='The file with the polygon points'
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
    polygon_points = points_from_file(outputs_file)

    plot_and_save(all_points, polygon_points, plots_file)


if __name__ == '__main__':
    main()
