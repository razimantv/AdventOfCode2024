# Day 21

[Problem link](https://adventofcode.com/2024/day/21)

The key insight is that, to press a button on pad i, all the previous pads need to be on `A`. So we can define `f(start, end, pad, n)` to be the 
```
Cost to go from:
  Start: start on pad n and A on next arrow pad
  End: (end, A) and press A
```

This turns it into a reachability problem. We can use Dijkstra's algorithm to solve this. Suppose we are at position `(p1, p2)` on the two pads. Moving to `(p1, q2)` and pressing it costs `f(q1, q2, 1, n - 1)`. We need to ensure that the keypress is valid and move `p1` as needed in response to the keypress.

We use the algorithm to find the minimum cost for all transitions on the final pad.
