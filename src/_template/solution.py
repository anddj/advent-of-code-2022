"""
https://adventofcode.com/2022/day/NN

>>> test_input_str = '''aaa
... bbb
... ccc'''
>>> main(test_input_str)
3
"""

from typing import Generator


def input_provider(input_str: str = None) -> Generator[str, None, None]:
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip()


def main(input_str: str = None) -> None:
    answer = 0
    for line in input_provider(input_str):
        answer += bool(line)

    print(answer)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
