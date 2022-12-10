"""
https://adventofcode.com/2022/day/10

>>> test_input_str = '''addx 15
... addx -11
... addx 6
... addx -3
... addx 5
... addx -1
... addx -8
... addx 13
... addx 4
... noop
... addx -1
... addx 5
... addx -1
... addx 5
... addx -1
... addx 5
... addx -1
... addx 5
... addx -1
... addx -35
... addx 1
... addx 24
... addx -19
... addx 1
... addx 16
... addx -11
... noop
... noop
... addx 21
... addx -15
... noop
... noop
... addx -3
... addx 9
... addx 1
... addx -3
... addx 8
... addx 1
... addx 5
... noop
... noop
... noop
... noop
... noop
... addx -36
... noop
... addx 1
... addx 7
... noop
... noop
... noop
... addx 2
... addx 6
... noop
... noop
... noop
... noop
... noop
... addx 1
... noop
... noop
... addx 7
... addx 1
... noop
... addx -13
... addx 13
... addx 7
... noop
... addx 1
... addx -33
... noop
... noop
... noop
... addx 2
... noop
... noop
... noop
... addx 8
... noop
... addx -1
... addx 2
... addx 1
... noop
... addx 17
... addx -9
... addx 1
... addx 1
... addx -3
... addx 11
... noop
... noop
... addx 1
... noop
... addx 1
... noop
... noop
... addx -13
... addx -19
... addx 1
... addx 3
... addx 26
... addx -30
... addx 12
... addx -1
... addx 3
... addx 1
... noop
... noop
... noop
... addx -9
... addx 18
... addx 1
... addx 2
... noop
... noop
... addx 9
... noop
... noop
... noop
... addx -1
... addx 2
... addx -37
... addx 1
... addx 3
... noop
... addx 15
... addx -21
... addx 22
... addx -6
... addx 1
... noop
... addx 2
... addx 1
... noop
... addx -10
... noop
... noop
... addx 20
... addx 1
... addx 2
... addx 2
... addx -6
... addx -11
... noop
... noop
... noop'''
>>> main(test_input_str)
13140
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
>>> main()
14360
###...##..#..#..##..####.###..####.####.
#..#.#..#.#.#..#..#.#....#..#.#.......#.
###..#....##...#..#.###..#..#.###....#..
#..#.#.##.#.#..####.#....###..#.....#...
#..#.#..#.#.#..#..#.#....#.#..#....#....
###...###.#..#.#..#.####.#..#.####.####.
"""

from typing import Generator
from collections import namedtuple


def input_provider(input_str: str = None) -> Generator[str, None, None]:
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip()


def run_signal_generator(input_str) -> Generator[int, None, None]:
    # Yield x_register value on each cycle
    x_register = 1
    cycles = {
        "noop": 1,
        "addx": 2,
    }
    Command = namedtuple("Command", "name arg", defaults=[None, None])
    for line in input_provider(input_str):
        cmd = Command(*line.split())
        for _ in range(cycles[cmd.name]):
            yield x_register
        if cmd.name == "addx":
            x_register += int(cmd.arg)


def main(input_str: str = None) -> None:

    signals_strengths_sum = 0
    signals_first_step = 20
    signals_steps = 40

    crt_screen_size = {"rows": 6, "columns": 40}
    crt = []

    for idx, x_register in enumerate(run_signal_generator(input_str)):
        cycle = idx + 1
        crt_current_row = idx // crt_screen_size["columns"]
        if len(crt) < crt_current_row + 1:
            crt.append([])
        crt_current_column = idx - crt_current_row * crt_screen_size["columns"]
        crt[crt_current_row].append(
            "#" if abs(crt_current_column - x_register) < 2 else "."
        )
        if not (cycle - signals_first_step) % signals_steps:
            signals_strengths_sum += cycle * x_register

    print(signals_strengths_sum)

    for i in range(crt_screen_size["rows"]):
        print("".join(crt[i]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
