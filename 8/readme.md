# Day 8

[Problem link](https://adventofcode.com/2024/day/8)

## Part 1

The antinodes for `(i1, j1)` and `(i2, j2)` are `(2 * i2 - i1, 2 * j2 - j1)` and `(2 * i1 - i2, 2 * j1 - j2)`. Just check whether the antinode is in the grid.

## Part 2

Use cross product to check collinearity: `(i, j)` lies on the line through (`i1, j1)` and `(i2, j2)` if and only if `(i - i1) * (j - j2) == (j - j1) * (i - i2)`.
