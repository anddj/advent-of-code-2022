"""

https://adventofcode.com/2022/day/4

>>> test_input = '''2-4,6-8
... 2-3,4-5
... 5-7,7-9
... 2-8,3-7
... 6-6,4-6
... 2-6,4-8'''
>>> main(test_input)
Part one answer is 2
Part two answer is 4
"""


def input_provider(input_str=None):
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for ll in f:
                yield ll


def get_ranges(r_str):
    def _make_range(range_str):
        [start, stop] = [int(i) for i in range_str.split('-')]
        return range(start, stop+1)
    [r1, r2] = [_make_range(s) for s in r_str.split(',')]
    return r1, r2


def main(input_data=None):
    subset_counter = intersection_counter = 0
    for line in input_provider(input_data):
        range1, range2 = get_ranges(line)
        subset_counter += set(range1).issubset(set(range2)) or set(range2).issubset(range1)

        intersection_counter += not set(range1).isdisjoint(set(range2))

    print("Part one answer is", subset_counter)
    print("Part two answer is", intersection_counter)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
