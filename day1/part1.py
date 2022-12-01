# Day 1, Part 1
# https://adventofcode.com/2022/day/1

max_number = 0
stack_sum = 0
INPUT_FILE = "input.lst"


with open(INPUT_FILE) as f:
    for line in f:
        if line != "\n":
            stack_sum += int(line)
        else:
            if not stack_sum:
                continue
            max_number = max(stack_sum, max_number)
            stack_sum = 0

if stack_sum:
    max_number = max(stack_sum, max_number)

print(max_number)

assert max_number == 69310
