### CodeWars XXVI - 26 - Factored

### Observation

* It was tempting to go ahead and just do the factoring, but this will need some thoughts since we will need to be able to expand each factor multiplications in descending order carefully.
* Be careful of time limit as well since the input mentioned 32-bit limit, which means we can go up to billions.  This means if we are not careful to factorize the number, we might run out of time.  A good square-root algorithm to factorize a number should suffice.  You want to test your solution with `1200000000`, for example, to see if your solution will finish in time.

### The Idea
We will formulate a function `solve(n)` which will accept `n` as the integer to factorize, and we will store all product of factors as asked by the problem.  We also will cache the result of the calculation so that we do not need to repeat any request with the same `n`.

Basically, for a number `n`, we will need the function to return an array of products of divisors.  For examples:
* `solve(4)` will give us: `[ [4], [2, 2] ]`,
* `solve(2)` will give us: `[ [2] ]`.

When calculating `solve(n)`, first start with a main result of `[n]` itself, then we find all factors of `n` in descending order.  For example, for `n = 16`, we start with `[ [16] ]` as the result and observe its factors (omitting 1 and 16): `[8, 4, 2]`.  We will have to process each factor in that order:
* With a factor 8, the other factor is 2 (that is, 16 / 8) and the further expanded factors can be seen in `solve(2)`, which happens to have only one result `[2]` in the returned array.  We produce `[8, 2]` in this iteration.
* With a factor 4, the other factor is 4 (that is, 16 / 4) and the further expanded factors can be seen in `solve(4)`, which happens to have `[4]` and `[2, 2]` in the array returned.  We produce `[4, 4]` and `[4, 2, 2]` and add them in the result of `solve(n)`.
* With a factor 2, the other factor is 8 (that is, 16 / 2) and the further expanded factors can be seen in `solve(8)`, which will give us `[8]`, `[4, 2]`, `[2, 2, 2]`.  But now, we won't use `[8]` nor `[4, 2]` since it contains numbers that are greater than our main factor 2 here.  So we will only care for `[2, 2, 2]`, and we produce `[2, 2, 2, 2]` here.

```python
cache = {}

def solve(n):
    if n in cache: return cache[n]
    f = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            f.append(d)
            other = n // d
            if other > d:
                f.append(other)
        d += 1
    f.sort(reverse=True)

    res = [[n]]
    for d in f:
        for next_arr in solve(n // d):
            if any(map(lambda x: x > d, next_arr)): continue
            arr = [d]
            arr.extend(next_arr)
            res.append(arr)

    cache[n] = res
    return res

def get_factors(arr):
    return f"({'*'.join(map(str, arr))})"

def solution(n, res):
    print(f"{n}=", end="")
    print(','.join(map(get_factors, res)))

for line in open(0):
    n = int(line)
    if n == 0: break
    res = solve(n)
    if len(res) > 1:
        solution(n, res[1:])
```
