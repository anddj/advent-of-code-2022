"""
https://adventofcode.com/2022/day/NN

>>> test_input_str = '''aaa
... bbb
... ccc'''
>>> main(test_input_str)
3
"""


def input_provider(input_str=None):
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for ll in f:
                yield ll.rstrip()


def main(input_str=None):
    answer = 0
    for line in input_provider(input_str):
        answer += bool(line)

    print(answer)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
