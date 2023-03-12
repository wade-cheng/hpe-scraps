### CodeWars XXVI - 28 - Trees in the Park

### Observation

* The maximum `N`, that is, the number of rows, the number of columns, and the number of gardens is maxed to 7.
* Each row needs to have exactly one tree, and each column also needs to have exactly one tree.
* Each garden needs to also have exactly one tree.
* There shouldn't be any pair of trees which are diagonally adjacent.

### The Idea

If you're using Python or C++, you'll be pampered with `itertools.permutations()` or `std::next_permutation()`, respectively.  From the fact that we can only have one tree per row (and also per column), we can operate on the permutation of `[0, 1, .. N-1]`.  For example, for `N = 4`, imagine all the permutations of `[0, 1, 2, 3]`, `[0, 1, 3, 2]`, `[0, 2, 1, 3]`, ... `[3, 2, 1, 0]` (all 24 of them).  Suppose you are dealing with: `[2, 3, 1, 0]`.  This means:
* For the first row, you'll plant a tree on column 2,
* For the second row, you'll plant a tree on column 3,
* For the third row, you'll plant a tree on column 1,
* For the fourth row, you'll plant a tree on column 0.

```text
..T.
...T
.T..
T...
```

*Note: You can also imagine an equivalent problem of placing `N` chess rooks on an `N x N` chess board in such a way that none of the rooks attack each other.*

The `itertools.permutations()` or `std::next_permutation()` will give you these permutations to check.  We then just need to validate whether that permutation is a good/valid one.

How to check if it's valid?  First of all, for each row, we check the row below it.  If the 2 trees in two adjacent rows (you can just check the two values in the permutation array) differ by exactly 1, that means they're diagonally adjacent, and it means not valid.

The second test to see if the permutation is valid, is to by adding each of the letters identified by the tree positions into a set!  If at the end of the checks the length of that set is the same as `N`, then it is a valid one because each garden has exactly one tree.  If the length of the set is less than `N`, it means there are 2 same letters being used in this permutation, which is not good.

```python
from itertools import permutations

n = int(input())
grid = [[x for x in input()] for _ in range(n)]

def solution(p):
    for i, j in enumerate(p):
        grid[i][j] = grid[i][j].upper()
        print(''.join(grid[i]))

for p in permutations(range(n)):
    valid = True
    gardens = set()
    for i, j in enumerate(p):
        if i+1 < n and abs(j-p[i+1]) == 1: valid = False
        gardens.add(grid[i][j])
    if valid and len(gardens) == n:
        solution(p)
        break
```
