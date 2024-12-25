# Day 16

[Problem link](https://adventofcode.com/2024/day/16)

## Part 1

Do a Dijkstra with (x, y, direction) as the state. Moving along the direction costs one unit but changing direction costs 1000. Find the minimum cost to reach endpoint for all possible directions.

## Part 2

Do a Dijkstra from the endpoint (all four directions together). For every cell, check whether the sum of distances from start and end for opposite directions is equal to the cost to reach the end from the start. This will happen if and obly if the cell is on the shorteat path to the end.
