### CodeWars XXVI - 30 - Escape the Fire

### Observation

* After careful observation, it should be apparent that this is a shortest path problem.
* The twist is that we have these valves on the empty rooms whose status (active or inactive) we will need to track.
* There can only be **at most 10 valves** in the grid (by the mention of the rooms on fire, `A .. J`).

### The Idea

*Note: If you haven't learned Breadth First Search (BFS), check this [Wikipedia article on BFS](https://en.wikipedia.org/wiki/Breadth-first_search) first.*

Formulating the *state* of the BFS is the key idea here.  Usually on a grid setup like this, the state would just be the cell coordinates, namely *row* and *column*.  But this time, it won't be enough.  We will need to add another attribute here into the state, that is, the state of each valve.  This also means that during the BFS run, we *might visit the same cells more than once*, but every duplicate visit to that same cell will need to have a **different open/closed states of the valves**.  The state of each valve can be open or close.  Since there can be at most 10 valves, this is like a binary value with 10-bits, or a tuple with 10 values in it (0 or 1 for each), or a string like `"000101011"` where `'0'` indicates inactive valve, and `'1'` indicates an active/open valve which means the corresponding room on fire is already neutralized.

This idea here will be using bitmasks and bitwise operations.  You can convert it to a tuple or string based information to track which valves are open/active.  *Note: Do NOT use a list/array as part of your state because list/array is not hashable, you'll get into bad situation if you do so.*

The starting state would then be `(r, c, m)` where `(r, c)` indicates the cell location of `'S'`, and `m` the starting state of all the valves, that is, 0 since all valves are closed in the beginning.  We then run BFS algorithm to find the shortest path from the starting state to the target state, that is, any state which has an `'X'` on its cell position.

The key things to evaluate to see if we can get to the adjacent neighbor (in the code below, the next state is denoted by `(rr, cc, mm)`, that is, the state that is one step away from the current one being evaluated) are:
* See if the state is invalid because it either goes out of bounds, or it contains a wall `'#'`.
* If this next state is actually a valve room (`'a' .. 'j'`), then make sure we update the mask to indicate that the corresponding valve is open.
* If this next state (after potentially adding an open valve, if applicable) is already seen before, we should skip adding it to the queue again.
* If this next state is a room on fire (`'A' .. 'J'`) and the corresponding valve to put out the fire has not been open, then you have to skip since you can't get there yet.

Additionally, maintain a dictionary of *previous state* which lead to this current state.  This is useful to reconstruct back the shortest path we are taking.

```python
rows, cols = map(int, input().split())
grid = [[x for x in input()] for _ in range(rows)]

def solution(r, c, m, pred):
    res = []
    while True:
        if grid[r][c].isalpha(): res.append(grid[r][c])
        if pred[(r, c, m)] is None: break
        r, c, m = pred[(r, c, m)]
    print(' '.join(res[::-1]))
    return True

def bit_for_valve(ch):
    return 1 << (ord(ch)-ord('a'))

def bit_for_fire(ch):
    return 1 << (ord(ch)-ord('A'))

def is_fire(r, c):
    return 'A' <= grid[r][c] <= 'J'

def is_valve(r, c):
    return 'a' <= grid[r][c] <= 'j'

def bfs(r, c, m):
    q, pred = [(r, c, m)], {(r, c, m): None}
    i = 0
    while i < len(q):
        r, c, m = q[i]
        i += 1

        if grid[r][c] == 'X':
            return solution(r, c, m, pred)

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            rr, cc, mm = r + dr, c + dc, m
            if rr < 0 or rr >= rows or cc < 0 or cc >= cols: continue                   # out of bounds
            if grid[rr][cc] == '#': continue                                            # impassable wall
            if is_valve(rr, cc):
                mm |= bit_for_valve(grid[rr][cc])
            if (rr, cc, mm) in pred: continue                                           # already seen this state
            if is_fire(rr, cc) and (mm & bit_for_fire(grid[rr][cc])) == 0: continue     # can't get into fire without valve

            q.append((rr, cc, mm))
            pred[(rr, cc, mm)] = (r, c, m)
    return False

for i in range(rows):
    if 'S' in grid[i]:
        bfs(i, grid[i].index('S'), 0)
        break
```
