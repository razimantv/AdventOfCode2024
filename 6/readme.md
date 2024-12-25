# Day 6

[Problem link](https://adventofcode.com/2024/day/6)

## Part 1

Keep (x, y, direction) as a state and move in the direction until we reach a wall (rotate direction) or leave the grid  (terminate). Mark all visited cells and return their count.

## Part 2

For every visited cell in part 1, turn it into a wall and repeat the process. We have a loop if any (x, y, direction) state is repeated.
