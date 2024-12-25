# Day 20

[Problem link](https://adventofcode.com/2024/day/20)

Using a  breadth first search, find the shortest distance from the start and end to all other vertices. This also gives the shortest path to the end. For every pair of vertices with Manhattan distance d within the cheat size limit, find the sum of distances of the two points from the start and end, added to d. This gives the new shortest path. Check whether it reduces the original shortest path length by the required amount.
