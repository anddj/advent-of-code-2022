"""
https://adventofcode.com/2022/day/15

>>> test_input_str = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
... Sensor at x=9, y=16: closest beacon is at x=10, y=16
... Sensor at x=13, y=2: closest beacon is at x=15, y=3
... Sensor at x=12, y=14: closest beacon is at x=10, y=16
... Sensor at x=10, y=20: closest beacon is at x=10, y=16
... Sensor at x=14, y=17: closest beacon is at x=10, y=16
... Sensor at x=8, y=7: closest beacon is at x=2, y=10
... Sensor at x=2, y=0: closest beacon is at x=2, y=10
... Sensor at x=0, y=11: closest beacon is at x=2, y=10
... Sensor at x=20, y=14: closest beacon is at x=25, y=17
... Sensor at x=17, y=20: closest beacon is at x=21, y=22
... Sensor at x=16, y=7: closest beacon is at x=15, y=3
... Sensor at x=14, y=3: closest beacon is at x=15, y=3
... Sensor at x=20, y=1: closest beacon is at x=15, y=3'''
>>> main(test_input_str, part1_y=10, part2_max=20)
26
56000011
>>> main(part1_y=2*10**6, part2_max=4*10**6)
4876693
11645454855041
"""

import re
from typing import Generator, Union, Callable


def input_provider(input_str: str = None) -> Generator[str, None, None]:
    if input_str:
        for s in input_str.split("\n"):
            yield s
    else:
        with open("input.txt", "r") as f:
            for line in f:
                yield line.rstrip()


def main(input_str: str = None, *, part1_y: int, part2_max: int) -> None:
    r = re.compile("-?\d+")
    data = []
    for line in input_provider(input_str):
        data.append([int(i) for i in r.findall(line)])

    # Part 1

    sensors = set()
    beacons = set()
    for idx, i in enumerate(data):
        if i[3] == part1_y:
            beacons.update({i[2]}) # beacons found on the line
        radius = abs(i[2] - i[0]) + abs(i[3]-i[1])
        y_dist = abs(part1_y - i[1])
        sensors.update(list(range(i[0] - radius + y_dist, i[0] + radius + 1 - y_dist)))

    sensors.difference_update(beacons) # sensors coverage minus beacons
    print(len(sensors))

    # Part 2

    def sensor_factory(sensor_pos: tuple, beacon_pos: tuple) -> Callable:
        rd = abs(beacon_pos[0] - sensor_pos[0]) + abs(beacon_pos[1] - sensor_pos[1])
        def get_x_increment(x_pos: int, y_pos: int) -> Union[int, None]:
            dist = abs(y_pos - sensor_pos[1])
            is_covered = (abs(x_pos - sensor_pos[0]) + abs(y_pos - sensor_pos[1])) <= rd
            if is_covered:
                return sensor_pos[0] - x_pos + rd - dist + 1

            return None

        return get_x_increment

    sensors = [sensor_factory((d[0], d[1]), (d[2], d[3])) for d in data]

    x = 0
    y = 0
    while True:
        counter = 0
        if y > part2_max:
            break
        for s in sensors:
            x_increment = s(x, y)
            if x_increment is not None:
                x += x_increment
                if x > part2_max:
                    # Next line
                    x = 0
                    y += 1
                break
            counter += 1
        if counter == len(data):  # the point is not covered by any sensor
            print(x * 4000000 + y)
            break

    return


if __name__ == "__main__":
    import doctest
    doctest.testmod()
