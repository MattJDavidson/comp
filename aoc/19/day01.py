#!/usr/bin/env python3
import sys


def fuel(weight: int):
    return weight // 3 - 2

def weighted_fuel(weight:int)-> int:
    weights = []
    while weight > 8:
        weight = fuel(weight)
        weights.append(weight)
    return sum(weights)

def main():
    lines = [int(_.strip()) for _ in open("inputs/01.txt", "r")]
    print(sum(map(fuel, lines)))
    print(sum(map(weighted_fuel, lines)))


if __name__ == "__main__":
    sys.exit(main())
