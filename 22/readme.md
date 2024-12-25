# Day 22

[Problem link](https://adventofcode.com/2024/day/22)

## Part 1

The transitions form a random number generator based on bit shifts. We just need to implement it and run it 2000 times.

## Part 2

While running the process, we can store the last four digit differences as a 20-bit mask. We add the first value for each mask in each run, and select the largest.
