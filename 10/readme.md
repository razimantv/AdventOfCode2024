# Day 10

[Problem link](https://adventofcode.com/2024/day/10)

## Part 1

Using memoised recursion, find the set of end points that can be reached from each cell. What we need is the sum of sizes of the sets for all 0-valued locations. Recursion involves taking the union of solutions for all children.

## Part 2

The only modification needed is to return the count instead of the set, and add the values of the children instead of taking the union.
