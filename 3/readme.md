# Day 3

[Problem link](https://adventofcode.com/2024/day/3)

## Part 1

Use the regex `r"mul\((\d{1,3}),(\d{1,3})\)"` to look for occurrences of `mul(a,b)` in the input string where `a` and `b` are 1-3 digit integers, and extract them.

## Part 2

More regexes: Find the locations of `do()` and `dont()` with regexes. Scan through the three lists together to ensure we know for each `mul` whether it follows a `do` or a `dont`.
