# Day 14

[Problem link](https://adventofcode.com/2024/day/14)

## Part 1

Use moduli to find where each robot ends up. It is then easy to count how many end up in each quadrant.

## Part 2

Heuristic: A real image will have more adjacent pixels than a random collection of pixels. So find the number of adjacent pixels for each time point up to 101x103 (after which the system repeats) and find the frame with the most adjacent pixels. Can be done efficiently by reusing a visited array.
