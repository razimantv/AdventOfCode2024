# Day 19

[Problem link](https://adventofcode.com/2024/day/19)

## Part 1

Define f(i) to be the number of ways to make the i-length prefix of target using given words. We start with f(0) = 1. If the substring[i:j] of target exists in the word list, increment f(j) by f(i). The target word can be made if f(size of target) is nonzero.

## Part 2

We need to find the sum of f(size(target)) for all target words.
