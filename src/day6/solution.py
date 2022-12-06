"""
https://adventofcode.com/2022/day/6

>>> main("bvwbjplbgvbhsrlpgdmjqwftvncz")
5
>>> main("nppdvjthqldpwncqszvftbrmjlhg")
6
>>> main("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
10
>>> main("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
11
>>> main("mjqjpqmgbljsphdztnvjfqwrcgsmlb", window_size=14)
19
>>> main("bvwbjplbgvbhsrlpgdmjqwftvncz", window_size=14)
23
>>> main("nppdvjthqldpwncqszvftbrmjlhg", window_size=14)
23
>>> main("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", window_size=14)
29
>>> main("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", window_size=14)
26
>>> main(window_size=4)
1140
>>> main(window_size=14)
3495
"""


def input_provider(input_str=None):
    if input_str:
        for s in input_str:
            yield s
    else:
        with open("input.txt", "rb") as f:
            while byte := f.read(1):
                yield byte


def main(input_str=None, *, window_size=4):
    answer = None
    buf = []
    for idx, letter in enumerate(input_provider(input_str)):
        if len(buf) < window_size:
            buf.append(letter)
            continue

        if len(set(buf)) == window_size:
            answer = idx
            break

        buf.append(letter)
        buf.pop(0)

    print(answer)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
