"""
https://adventofcode.com/2022/day/11

>>> test_input_str = '''Monkey 0:
...   Starting items: 79, 98
...   Operation: new = old * 19
...   Test: divisible by 23
...     If true: throw to monkey 2
...     If false: throw to monkey 3
...
... Monkey 1:
...   Starting items: 54, 65, 75, 74
...   Operation: new = old + 6
...   Test: divisible by 19
...     If true: throw to monkey 2
...     If false: throw to monkey 0
...
... Monkey 2:
...   Starting items: 79, 60, 97
...   Operation: new = old * old
...   Test: divisible by 13
...     If true: throw to monkey 1
...     If false: throw to monkey 3
...
... Monkey 3:
...   Starting items: 74
...   Operation: new = old + 3
...   Test: divisible by 17
...     If true: throw to monkey 0
...     If false: throw to monkey 1'''
>>> main(test_input_str, part=1)
10605
>>> main(part=1)
58056
>>> main(test_input_str, part=2)
2713310158
>>> main(part=2)
15048718170
"""



import re
import math
from typing import Generator, Callable, Iterable


DIVISORS = set()


def input_provider(input_str: str = None) -> Generator[str, None, None]:
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip()


class Monkey:
    items: list
    operation: str
    test_f: Callable
    inspections_count: int = 0
    divisor: int

    def __init__(self, data: list) -> None:
        """Constructor

        Parsing monkey data structure e.g.:
        [0] Monkey 0:
            [1] Starting items: 79, 98
            [2] Operation: new = old * 19
            [3] Test: divisible by 23
            [4] If true: throw to monkey 2
            [5] If false: throw to monkey 3
        """

        d_pattern = re.compile(r"\d+")

        self.items = list(map(int, d_pattern.findall(data[1])))
        self.operation = data[2].split("=")[1].lstrip()

        # Construct divisor test function
        divisor = int(d_pattern.search(data[3])[0])
        self.divisor = divisor
        DIVISORS.add(divisor)
        true_res = int(d_pattern.search(data[4])[0])
        false_res = int(d_pattern.search(data[5])[0])
        self.test_f = lambda x: false_res if x % divisor else true_res

    def add_item(self, item: int) -> None:
        self.items.append(item)

    def run_test(self, part=1) -> list[(int, int)]:
        res = []
        self.inspections_count += len(self.items)
        for _ in range(len(self.items)):
            item = self.items.pop(0)
            op_str = self.operation.replace("old", str(item))
            i = eval(op_str)
            if part == 1:
                i //= 3
            elif part == 2:
                i %= math.prod(DIVISORS)  # modulo of the least common multiple
            res.append((self.test_f(i), i))

        return res


def main(input_str: str = None, *, part=1) -> None:
    monkeys = []
    monkey_data = []

    for line in input_provider(input_str):

        if line == "\n" or line == "":
            monkey = Monkey(monkey_data)
            monkeys.append(monkey)
            monkey_data = []
            continue

        monkey_data.append(line)

    # Flush the rest
    if monkey_data:
        monkey = Monkey(monkey_data)
        monkeys.append(monkey)

    rounds = 20 if part == 1 else 10000

    for _ in range(rounds):
        for monkey in monkeys:
            res: [(int, int)] = monkey.run_test(part=part)
            for monkey_update in res:
                monkey_index, item = monkey_update
                monkeys[monkey_index].add_item(item)

    inspections = [monkey.inspections_count for monkey in monkeys]
    monkey_business = math.prod(sorted(inspections)[-2:])
    print(monkey_business)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
