# https://adventofcode.com/2022/day/3

priorities_sum = 0


def get_item_priority(item):
    if ord("a") <= ord(item) <= ord("z"):
        priority = ord(item) - ord("a") + 1
    else:
        priority = ord(item) - ord("A") + 27
    return priority


with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        half = int(len(line) / 2)
        p1, p2 = set(line[:half]), set(line[half:])
        intersection = next(iter(p1.intersection(p2)))
        priorities_sum += get_item_priority(intersection)

print(priorities_sum)

assert priorities_sum == 8298
