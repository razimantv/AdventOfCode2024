# Day 24

[Problem link](https://adventofcode.com/2024/day/24)

## Part 1

Find the values for the variables starting with z by evaluating the rules recursively. 

## Part 2

The operations around the ith bit of an adder look like
```
s(i) = x(i) XOR y(i)
c(i) = x(i) AND y(i)
out(i) = s(i) XOR carry(i-1)
C(i) = carry(i-1) AND s(i)
carry(i) = C(i) OR c(i)
```
For every bit, check whether these operations are consistent with the given rules. Every failure gives us a pair of swapped outputs that can be identified manually.
