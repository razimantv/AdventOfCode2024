# Day 11

[Problem link](https://adventofcode.com/2024/day/11)

Define `f(n, d)` as the number of terms we will end up with after `d` days if we start with the number `n`. It is equal to the sum `f(m, d-1)` for all `m` that `n` splits into. Memoise to avoid recomputation.
