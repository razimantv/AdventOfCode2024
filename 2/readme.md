# Day 2

[Problem link](https://adventofcode.com/2024/day/2)

## Part 1

It is enough to check that for each line, all the adjacent differences lie in [-3, -1] or [1, 3]. Done by checking the minimum and maximum of the set of differences.

## Part 2

Brute force: For each element in the list, check whether removing it makes the list valid (check as in part 1).
