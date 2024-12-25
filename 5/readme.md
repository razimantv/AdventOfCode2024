# Day 5

[Problem link](https://adventofcode.com/2024/day/5)

## Part 1

Transform the edges into an adjacency list: For each vertex, keep a set of vertices it has edges to. In each line, check every pair of vertices to ensure that there is no backward edge.

## Part 2

For lines with a backward edge, create a fixed sequence by "insertion sort". To add a vertex to a "sorted" sequence, place it before the first vertex it has an edge to.
