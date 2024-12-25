# Day 12

[Problem link](https://adventofcode.com/2024/day/12)

## Part 1

Do a depth-first search to flood fill and find sizes of connected components. For each cell in the component, also count during dfs how many neighbours are outside the grid/in a different component to find the perimeter.

## Part 2

While finding the perimeter, if a horizontal border cell has its upper neighbour as a border cell as well, ignore it. Similarly for vertical border and left neighbour. This results in counting number of perimeter sections instead of perimeter.
