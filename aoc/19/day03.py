#!/usr/bin/env python3
import sys
from collections import defaultdict
from itertools import product
from typing import Tuple, Set

DIRECTIONS = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0),
}

Point = Tuple[int, int]


def track_wire_path(line: str):
    step_count = {}
    path = set()
    pos = (0, 0)
    steps = 0
    for movement in line.split(","):
        direction, repeat = movement[0], movement[1:]
        pos_delta = DIRECTIONS[direction]
        for _ in range(int(repeat)):
            pos = (pos[0] + pos_delta[0], pos[1] + pos_delta[1])
            steps += 1
            if pos not in step_count:
                step_count[pos] = steps
            path.add(pos)
    return path, step_count


def main():
    input = [_ for _ in open("inputs/03.txt", "r")]

    path_1, steps_1 = track_wire_path(input[0])
    path_2, steps_2 = track_wire_path(input[1])
    crossing_points = set.intersection(path_1, path_2)
    print(min([abs(x) + abs(y) for x, y in crossing_points]))
    print(min([steps_1[x, y] + steps_2[x, y] for x, y in crossing_points]))


if __name__ == "__main__":
    sys.exit(main())
