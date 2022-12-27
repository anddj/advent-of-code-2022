"""
https://adventofcode.com/2022/day/13

>>> test_input_str = '''[1,1,3,1,1]
... [1,1,5,1,1]
...
... [[1],[2,3,4]]
... [[1],4]
...
... [9]
... [[8,7,6]]
...
... [[4,4],4,4]
... [[4,4],4,4,4]
...
... [7,7,7,7]
... [7,7,7]
...
... []
... [3]
...
... [[[]]]
... [[]]
...
... [1,[2,[3,[4,[5,6,7]]]],8,9]
... [1,[2,[3,[4,[5,6,0]]]],8,9]'''
>>> main(test_input_str)
13
140
>>> main()
6428
22464
"""

from typing import Generator
from functools import cmp_to_key


def input_provider(input_str: str = None) -> Generator[str, None, None]:
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip()


def compare(left: "int | list", right: "int | list") -> int:
    res = 0
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    if not len(left):
        return 1

    for idx in range(len(left)):
        if idx > len(right) - 1:
            return -1
        if [type(left[idx]), type(right[idx])] == [int, int]:
            if left[idx] - right[idx]:
                return {True: 1, False: -1}[left[idx] < right[idx]]
            if len(left) < len(right) and idx == len(left) - 1:
                return 1
        else:
            if left[idx] == right[idx]:
                continue
            res = compare(left[idx], right[idx])
            if res in [-1, 1]:
                return res

    return res


def main(input_str: str = None) -> None:
    data = []
    buf = []
    for line in input_provider(input_str):
        if line == "":
            data.append(buf[:])
            buf = []
            continue
        buf.append((eval(line)))

    if len(buf):
        data.append(buf[:])

    idx_sum = 0
    all_members = []
    for idx, pair in enumerate(data, 1):
        all_members += pair
        res = compare(*pair)
        if res in (0, 1):
            idx_sum += idx

    divider_packets = ([[2]], [[6]])
    sorted_list = sorted(all_members + [*divider_packets],
                         key=cmp_to_key(compare), reverse=True)

    print(idx_sum)
    print(
        (sorted_list.index(divider_packets[0])+1)
        *
        (sorted_list.index(divider_packets[1])+1)
    )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
