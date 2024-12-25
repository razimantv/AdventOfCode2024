# Day 23

[Problem link](https://adventofcode.com/2024/day/23)

## Part 1

Create an adjacency list: For each vertex, store all the vertices connected to it bidirectionally.

For each vertex starting with t, loop through all pairs of its neighbours. If they have an edge between them, put the triplet into a set after ordering it. Find the size of the set in the end.

## Part 2

We find the largest clique in the graph by backtracking. Given a clique, for every vertex connected to the last vertex of the clique, check if it is connected to all the other vertices of the clique as well. If so, add it and recurse.
