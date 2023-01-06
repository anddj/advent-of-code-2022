"""
https://adventofcode.com/2022/day/14

>>> test_input_str = '''498,4 -> 498,6 -> 496,6
... 503,4 -> 502,4 -> 502,9 -> 494,9'''
>>> main(test_input_str)
24
93
>>> main()
745
27551
"""

from typing import Generator
from collections import namedtuple

grid = None


def input_provider(input_str: str = None) -> Generator[str, None, None]:
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip()


def init_y_pos(y):
    global grid
    if y not in grid:
        grid[y] = set()


def add_to_grid(line: str) -> None:
    global grid

    positions = line.split("->")

    for end_pos in range(1, len(positions)):
        end_x, end_y = eval(positions[end_pos])
        start_x, start_y = eval(positions[end_pos - 1])
        moving_along_axis = ("x", "y")[
            abs((end_x - start_x, end_y - start_y).index(0) - 1)
        ]
        if moving_along_axis == "x":
            init_y_pos(start_y)
            direction = 1 if end_x > start_x else -1
            grid[start_y].update(
                set(range(start_x, end_x + direction, direction))
            )
        else:
            direction = 1 if end_y > start_y else -1
            for i in range(start_y, end_y + direction, direction):
                init_y_pos(i)
                grid[i].update({start_x})


def main(input_str: str = None) -> None:
    global grid

    grid = {}
    for line in input_provider(input_str):
        add_to_grid(line)

    Pos = namedtuple("Pos", "x y")

    max_y = sorted(grid.keys())[-1]
    start_pos = Pos(500, 0)
    current_pos = start_pos
    came_to_rest_counter = 0
    falls_into_abyss_at = None

    while True:

        if falls_into_abyss_at is None and current_pos.y > max_y:
            falls_into_abyss_at = came_to_rest_counter

        if current_pos.y == max_y + 1:  # came to rest on the floor
            init_y_pos(current_pos.y)
            grid[current_pos.y].update({current_pos.x})
            current_pos = start_pos
            came_to_rest_counter += 1
            continue

        next_y = current_pos.y + 1

        if next_y not in grid:  # no obstacle, free fall ;)
            current_pos = Pos(current_pos.x, next_y)
            continue

        shift_x = 0, -1, 1
        moved = False
        for i in shift_x:
            if current_pos.x + i not in grid[next_y]:
                current_pos = Pos(current_pos.x + i, next_y)
                moved = True
                break
        if moved:
            continue

        init_y_pos(current_pos.y)
        grid[current_pos.y].update({current_pos.x})
        came_to_rest_counter += 1
        if current_pos == start_pos:  # source of the sand is blocked
            break
        current_pos = start_pos

    print(falls_into_abyss_at)
    print(came_to_rest_counter)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
