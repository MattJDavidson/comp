#!/usr/bin/env python3
import sys
from itertools import product


def execute_code(original_code, r1, r2):

    code = original_code[:]
    code[1] = r1
    code[2] = r2
    for i in range(0, len(code) - 1, 4):
        symbol, i1, i2, pos = code[i], code[i + 1], code[i + 2], code[i + 3]
        if symbol == 1:
            code[pos] = code[i1] + code[i2]
        elif symbol == 2:
            code[pos] = code[i1] * code[i2]
        else:
            break
    return code[0]


def main():
    test_input = list(map(int, [_.split(",") for _ in open("inputs/02.txt", "r")][0]))
    print(execute_code(test_input, 12, 2))
    for r1, r2 in product(range(100), range(100)):
        if execute_code(test_input, r1, r2) == 19690720:
            print(100 * r1 + r2)


if __name__ == "__main__":
    sys.exit(main())
