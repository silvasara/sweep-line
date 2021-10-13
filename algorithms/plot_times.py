#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import argparse
from pathlib import Path
from math import log10

sns.set_theme(style="ticks")
sns.set_palette(["#386cb0", "#e7298a"])


def plot_and_save(input_file, output_file, size):
    df = pd.read_csv(input_file)

    df['Tamanho'] = df.pop('tamanho').astype('int')
    df = df[['Tamanho', 'C++', 'Python']]

    size = list(map(float, size.lower().split('x')))
    fig = plt.figure(figsize=size)

    ax = fig.add_subplot()

    df.plot.bar(
        title='Tempos de execução',
        ax=ax,

        x='Tamanho',
        xlabel='Tamanho da entrada',
        rot=0,

        ylabel='Tempo (s)',
        logy=True,
    )

    def x_formatter(value):
        value = int(value.get_text())

        if value % 10 != 0 or value < 0:
            return 'invalid value'

        # set_major_formatter were not giving the real value
        return "$10^{%d}$" % log10(value) if value != 0 else "$10^0$"

    ax.set_xticklabels([x_formatter(v) for v in ax.get_xticklabels()])

    ax.grid()

    plt.tight_layout()

    fig.savefig(output_file, format="pgf")

    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description='Plot the execution times'
    )
    parser.add_argument(
        'inputs_file',
        type=str,
        help='The CSV file with all the times to be plotted. '
             'Columns: tamanho,C++,Python'
    )
    parser.add_argument(
        'outputs_file',
        type=str,
        help='The name/path of the PGF file to be created'
    )

    parser.add_argument(
        '--size',
        type=str,
        default='5x5',
        help='The size of the image in inches e.g. 5x5'
    )

    args = parser.parse_args()

    input_file = Path(args.inputs_file)
    output_file = Path(args.outputs_file)

    plot_and_save(input_file, output_file, args.size)


if __name__ == '__main__':
    main()
