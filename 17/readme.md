# Day 17

[Problem link](https://adventofcode.com/2024/day/17)

## Part 1

It can be seen that each step prints a 3-bit number, right shifts the input by 3 bits, and continues until it becomes 0. All we need to do is find the function that geberates the 3-bit number.

## Part 2

The above property implies that we can build up the result 3-bit by 3-bit. The first 3 bits of input should give the last output. Find all possibilities. Extend each valid solution by all 3-bit numbers. Find which ones generate the penultimate output and so on. We select the smallest possibility that creates the full output.
