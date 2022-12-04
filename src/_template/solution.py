"""
https://adventofcode.com/2022/day/NN

>>> test_input_str = '''Enter
... your
... test
... string
... here'''
>>> main(test_input_str)
Part one answer is 5
Part two answer is 5
>>> main()
Part one answer is 3
Part two answer is 3
"""


def input_provider(input_str=None):
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for ll in f:
                yield ll


def main(input_str=None):
    answer_1_aggregator = answer_2_aggregator = 0
    for line in input_provider(input_str):
        answer_1_aggregator += bool(line)
        answer_2_aggregator += bool(line)

    print("Part one answer is", answer_1_aggregator)
    print("Part two answer is", answer_2_aggregator)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
