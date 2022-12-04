# https://adventofcode.com/2022/day/3

priorities_sum = 0
stack = []


def get_item_priority(item):
    if ord("a") <= ord(item) <= ord("z"):
        priority = ord(item) - ord("a") + 1
    else:
        priority = ord(item) - ord("A") + 27
    return priority


def update_priorities_sum():
    global priorities_sum, stack
    intersection = stack[0].intersection(stack[1], stack[2])
    intersection = next(iter(intersection))
    priorities_sum += get_item_priority(intersection)


with open("input.txt", "r") as f:
    for line in f:
        if len(stack) == 3:
            update_priorities_sum()
            stack = [set(line.rstrip())]
            continue
        stack.append(set(line.rstrip()))

if len(stack):
    update_priorities_sum()

print(priorities_sum)

assert priorities_sum == 2708
