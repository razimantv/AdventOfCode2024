# Day 7

[Problem link](https://adventofcode.com/2024/day/7)

## Part 1

Starting with the first element, iteratively build all possible results after first i terms. The transition from i to i + 1 is done by combining all possible values after i operations with the i+1th value by addition and multiplication. The result is stored in a set to avoid duplicates. Just need to check in the end if the target value is in the set.

## Part 2

Repeat, with concatenation added as an operation.
