"""
https://adventofcode.com/2022/day/8

>>> test_input_str = '''30373
... 25512
... 65332
... 33549
... 35390'''
>>> main(test_input_str)
21
8
>>> main()
1713
268464
"""

from typing import Generator


def input_provider(input_str: str = None) -> Generator[str, None, None]:
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for ll in f:
                yield ll.rstrip()


def get_first_index(lst: [int], n: int) -> int:
    # Get the first index of the equal or higher height
    for idx, i in enumerate(lst):
        if i >= n:
            return idx
    return len(lst) - 1


def analyze(idx: int, nums: [int]) -> (bool, int):
    # Analyze `nums` list at the position `idx` in
    # left and right directions (1 dimensional search)

    # Get visibility in left and right directions
    is_visible_from_left = max(nums[:idx], default=-1) < nums[idx]
    is_visible_from_right = max(nums[idx + 1:], default=-1) < nums[idx]

    # Distance to the first same or higher tree
    try:
        dist_left = get_first_index(nums[:idx][::-1], nums[idx]) + 1
    except ValueError:
        dist_left = 0
    try:
        dist_right = get_first_index(nums[idx + 1:], nums[idx]) + 1
    except ValueError:
        dist_right = 0

    visible = is_visible_from_left or is_visible_from_right

    return visible, dist_left * dist_right


def run_grid(grid: list) -> tuple:
    scenic_score_multipliers = []
    visibility_data = []
    for lst in grid:
        visibility = []
        multipliers_group = []
        for i in range(len(lst)):
            is_visible, multiplier = analyze(i, lst)
            visibility.append(is_visible)
            multipliers_group.append(multiplier)
        scenic_score_multipliers.append(multipliers_group)
        visibility_data.append(visibility)

    return visibility_data, scenic_score_multipliers


def main(input_str: str = None):

    grid = []

    for line in input_provider(input_str):
        grid.append([int(i) for i in line])

    transposed_grid = [
        [grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))
    ]

    visibility_data_h, scenic_score_h = run_grid(grid)
    visibility_data_v, scenic_score_v = run_grid(transposed_grid)

    part1_answer = 0
    for x, i in enumerate(visibility_data_h):
        for y in range(len(i)):
            part1_answer += visibility_data_h[x][y] or visibility_data_v[y][x]

    part2_answer = 0
    for x, i in enumerate(scenic_score_h):
        for y in range(len(i)):
            product = scenic_score_h[x][y] * scenic_score_v[y][x]
            part2_answer = max(product, part2_answer)

    print(part1_answer)
    print(part2_answer)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
