# Day 9

[Problem link](https://adventofcode.com/2024/day/9)

## Part 1

Make an array of the spaces on the disk, populated by file ids or -1 if empty. Scan with two pointera from left and right. Whenever left is empty and right is a file, swap.

## Part 2

**Brute force**: Make two lists of spaces (position, size pairs) and files (position, size, id tuples). Scan file list from right to left, finding the first slot where it can be placed by scanning the space list. Edit/remove the space as needed when done.

**Better solution**: Use a segment tree of interval maxima for space sizes to find the first slot where a file can be placed using binary search. When a file is placed, update the segment tree.
