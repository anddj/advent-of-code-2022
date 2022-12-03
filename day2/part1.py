# https://adventofcode.com/2022/day/2

INPUT_FILE = "input.txt"
total_score = 0

WIN, LOOSE, DRAW = 6, 0, 3
[ROCK, PAPER, SCISSORS] = range(3)
OPPONENT_CHOICES = ["A", "B", "C"]
MY_CHOICES = ["X", "Y", "Z"]


def get_element_weights(shift_num):
    weights = [4, 2, -4]
    for i in range(shift_num):
        weights.insert(0, weights.pop())
    return weights


def play(opponent_choice, my_choice):
    if opponent_choice == my_choice:
        return DRAW

    element_weights = get_element_weights(opponent_choice)
    return element_weights[opponent_choice] + element_weights[my_choice]


assert play(ROCK, PAPER) == WIN
assert play(ROCK, SCISSORS) == LOOSE
assert play(ROCK, ROCK) == DRAW

assert play(PAPER, PAPER) == DRAW
assert play(PAPER, SCISSORS) == WIN
assert play(PAPER, ROCK) == LOOSE

assert play(SCISSORS, PAPER) == LOOSE
assert play(SCISSORS, SCISSORS) == DRAW
assert play(SCISSORS, ROCK) == WIN

with open(INPUT_FILE, "r") as f:
    for line in f:
        opponent_choice, my_choice = line.rstrip().split()
        total_score += play(OPPONENT_CHOICES.index(opponent_choice), MY_CHOICES.index(my_choice))
        total_score += MY_CHOICES.index(my_choice) + 1

print(total_score)

assert total_score == 10816
