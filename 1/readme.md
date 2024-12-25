# Day 1

[Problem link](https://adventofcode.com/2024/day/1)

## Part 1

We just need to sort the two columns and then find the sum of absolute differences between the two sorted columns

## Part 2

We need to multiply each value in the first column with its number of occurences in the second column and then sum them up. This is equivalent to summing after multiplying every unique number with its products of counts in the two columns, which can be evaluated with apython Counter.
