### CodeWars XXVI - 24 - Grid Hid

### Observation

* Word search problem.
* Need to return all the missing and found word list, the list shall be printed in ascending alphabetical order.
* Be careful that the grid dimension is specified in the order of *width*, then *height*.
* Also be careful in case the list is *empty*, the problem description does not explain what to do there, but probably better to ensure there is no trailing spaces (e.g., `"FOUND: "` should be trimmed to `"FOUND:"`)).

### The Idea
We get all the words first since they are specified earlier than the grid in the input file.  Then read the word search grid.

```python
cols, rows = map(int, input().split())
words = []
while True:
    w = input()
    if w == 'END': break
    words.append(w)

grid = [input() for _ in range(rows)]

```

After we got all info, we maintain 2 lists for *found* and *missing* words.  Go through each word and *search* them and bucket them to the correct list.
Now we only need to fill in the details on *how* to search the word.

The idea is:
* Do a loop of to examine each cell (two dimensional loop of row and column should suffice)
* For each starting cell, check 8 directions.  Always use a directional displacement (check the code below, I named it `dr` and `dc`) to walk the letters in the desired direction.
* For each direction, try to traverse each letter of the word according to the direction, if the walk goes out of bounds and the word has not been completely traversed, then the word is not found yet in that direction.  Similarly, if the expected letter on any position differs than what is on the grid during the walk, it means a mismatch.
* When we are able to traverse each letter of the searched word completely in any of the 8 directions, we can return `True` to indicate that the searched word is indeed found on the grid.

```python
def search(w):
    for i in range(rows):
        for j in range(cols):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0: continue
                    r, c = i, j
                    valid = True
                    for x in w:
                        if r < 0 or r >= rows or c < 0 or c >= cols or x != grid[r][c]:
                            valid = False
                            break
                        r, c = r + dr, c + dc
                    if valid: return True
    return False

found, missing = [], []
for w in words:
    if search(w):
        found.append(w)
    else:
        missing.append(w)
print(f"FOUND: {', '.join(sorted(found))}".strip())
print(f"MISSING: {', '.join(sorted(missing))}".strip())
```
