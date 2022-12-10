"""
https://adventofcode.com/2022/day/9

>>> test_input_str = '''R 4
... U 4
... L 3
... D 1
... R 4
... D 1
... L 5
... R 2'''
>>> test_input_str_large = '''R 5
... U 8
... L 8
... D 3
... R 17
... D 10
... L 25
... U 20'''
>>> main(test_input_str, rope_length=2)
13
>>> main(rope_length=2)
6354
>>> main(test_input_str, rope_length=10)
1
>>> main(test_input_str_large, rope_length=10)
36
>>> main(rope_length=10)
2651
"""

from typing import Generator

"""
Let's describe moves in these coordinates:
   C1 C2 C3
R1 x  x  x
R2 x  x  x
R3 x  x  x
"""
MOVES = {
    # "direction": (row_change, column_change)
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}


def input_provider(input_str: str = None) -> Generator[str, None, None]:
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for line in f:
                if line == "\n":
                    break
                yield line.rstrip()


def change_position(current_position: tuple, direction: str) -> tuple:
    return tuple(map(sum, zip(current_position, MOVES[direction])))


def is_near(pos1: tuple, pos2: tuple) -> bool:
    """Check if two positions are touching,
       whether horizontally, vertically or diagonally"""
    return tuple(map(lambda x: abs(x[0]-x[1]) < 2, zip(pos1, pos2))) == (True, True)


def get_follow_up_position(head: tuple, tail: tuple) -> tuple:
    """Find the new tail position after head position changes"""
    row_delta, col_delta = map(lambda x: x[0]-x[1], zip(head, tail))
    lst = list(tail)
    if abs(row_delta) < abs(col_delta):
        lst[0] += row_delta
        lst[1] += 1 if col_delta > 0 else -1
    elif abs(row_delta) > abs(col_delta):
        lst[1] += col_delta
        lst[0] += 1 if row_delta > 0 else -1
    else:  # equal, should follow diagonally
        lst[0] += -1 if row_delta < 0 else 1
        lst[1] += -1 if col_delta < 0 else 1

    return tuple(lst)


def main(input_str: str = None, *, rope_length: int = 2) -> None:
    start_position = (0, 0)
    rope_knots_positions = [start_position] * rope_length
    tail_visited_positions = {start_position}
    for lst in input_provider(input_str):
        direction, steps = lst.split()
        for _ in range(int(steps)):
            rope_knots_positions[0] = change_position(rope_knots_positions[0], direction)
            for knot in range(1, rope_length):
                [head_knot, tail_knot] = rope_knots_positions[knot-1:knot+1]
                if not is_near(head_knot, tail_knot):
                    rope_knots_positions[knot] = \
                        get_follow_up_position(head_knot, tail_knot)
            tail_visited_positions.add(rope_knots_positions[rope_length-1])

    print(len(tail_visited_positions))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
