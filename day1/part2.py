# Day 1, Part 2
# https://adventofcode.com/2022/day/1

stack_sum = 0
biggest_stacks = [0, 0, 0]
INPUT_FILE = "input.lst"


def update_biggest_stacks(new_stack_sum):
    global biggest_stacks
    biggest_stacks.append(new_stack_sum)
    biggest_stacks.sort(reverse=True)
    biggest_stacks = biggest_stacks[:3]


with open(INPUT_FILE) as f:
    for line in f:
        if line != "\n":
            stack_sum += int(line)
        else:
            if not stack_sum:
                continue
            update_biggest_stacks(stack_sum)
            stack_sum = 0

if stack_sum:
    update_biggest_stacks(stack_sum)

print(sum(biggest_stacks))

assert sum(biggest_stacks) == 206104
