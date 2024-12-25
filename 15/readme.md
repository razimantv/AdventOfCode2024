# Day 15

[Problem link](https://adventofcode.com/2024/day/15)

## Part 1

Keep moving in the direction until we hit a wall or a space. If a wall, this move cannot be performed. Otherwise translate the entire chunk until the space by one unit.

## Part 2

Do a breadth first search starting from initial position to find all `[]` cells it can push, by adding the paired bracket to the queue as well. If any wall is pushed, the move cannot be performed. Otherwise all `[]` cells need to move by one unit.
