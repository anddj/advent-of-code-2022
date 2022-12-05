"""
https://adventofcode.com/2022/day/5

>>> main(mode="part1")
FRDSQRRCD
>>> main(mode="part2")
HRFTQVWNN
"""

import re


def input_provider(input_str=None):
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for ll in f:
                yield ll


def parse_stacks_line(line):
    stack = []
    for i in range(len(line)//4):
        stack.append(line[i*4+1])
    return stack


def main(input_str=None, *, mode="part1"):
    # Parse crates location
    stack = []
    for line in input_provider(input_str):
        if line[:2] != " 1":
            stack.append(parse_stacks_line(line))
        else:
            break
    crates = []
    for i in range(len(stack[0])):
        crates.append([])
    for i in stack:
        for idx, ii in enumerate(i):
            if ii != " ":
                crates[idx].append(ii)
    for i in crates:
        i.reverse()

    # Parse movements
    movements = []
    for line in input_provider(input_str):
        if line[:5] == "move ":
            res = re.search(r"^move\s([0-9]+)\sfrom\s([0-9]+)\sto\s([0-9]+)$", line)
            movements.append((res.groups()))

    # Perform movements
    for m in movements:
        moves = [int(i) for i in m]
        if mode == "part1":
            for i in range(moves[0]):
                crates[moves[2]-1].append(crates[moves[1]-1].pop())
        else:
            temp = []
            for i in range(moves[0]):
                temp.append(crates[moves[1] - 1].pop())
            temp.reverse()
            crates[moves[2] - 1].extend(temp)

    # Output the answer
    ans = []
    for i in crates:
        ans.append(i.pop())
    print("".join(ans))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
