### CodeWars XXVI - 27 - Amgine's Cypher

### Observation

* The number of dials is always 3, and each dial can go up to 60 possibilities (1 thru 60).
* Brute forcing the initial position of dials A, B, C is the easy solution here.  Each sentence to decode will always incur 60<sup>3</sup> possible dial combinations, and for each it will construct a new sentence, could be up to 80 letters.  If the judge allows runtime for, say, 20-30 seconds, then brute force should be the way to go to do in the contest since it is easier to code.

### The Idea
Brute-forcing the starting value of A, B, and C seems to be the easiest idea to implement, and short implementation too.
Decoding and encoding are symmetrical, so we really just need to formulate the function `decode(w, a, b, c)` where `w` is the word to decode, and `a`, `b`, and `c` are the current positions of the dials.  We just need to follow the instruction on how to:
* calculate the new letter, and
* how to rotate the dials for the next letter decoding.

```python
n = int(input())

def increment(x):
    x += 1
    if x > n: x = 1
    return x

def decode(w, a, b, c):
    res = ''
    for x in w:
        if x.isalpha():
            idx = 26 - ((ord(x)-ord('A') +1 + a + b + c) % 26)
            res += chr(ord('A')-1+idx)
            if b % 3 == 0: a = increment(a)
            if c % 5 == 0: b = increment(b)
            c = increment(c)
        else:
            res += x
    return res

def brute_force(w):
    for a in range(1, n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):
                msg = decode(w, a, b, c)
                if 'AMGINE' in msg:
                    print(a, b, c)
                    print(msg)
                    return True
    return False

while True:
    w = input()
    if w == ".": break
    brute_force(w)
```

Another idea, which is a smarter brute force is to basically precalculate all possible encoded `"AMGINE"`s.  This will save time to not have to decode the whole sentence before finding if it contains the encoded `"AMGINE"` in it.  With this approach, you will:
* First save all possible encoded `"AMGINE"`s and use it as key to a dictionary which will give you the combination of A, B, C to produce such an encoded `"AMGINE"`.
* Now, for each sentence to decode, we check out which encoded `"AMGINE"` is present in the sentence.  Pick the matching one, and we then readily have the A, B, C state at the beginning of `"AMGINE..."` sequence.
* Since this encoded `"AMGINE"` can be found anywhere in the encoded sentence, we need to backtrack the dial situation until the very first letter, ... this is quite simple, just reverse the dial rotation algorithm:
  * Moving backwards towards index 0, for each letter position, we can:
    * decrement C first,
    * if C is multiple of 5, decrement B
    * if B is multiple of 3, decrement A
  * Stop when you got to index 0, the current A, B, C values are the good starting position, print it.
  * Decode forward the whole sentence using this A, B, C position, print it.

This code below should run **faster** than the previous brute force.  Note that this is still a brute force, just a bit smarter.

```python
n = int(input())

def increment(x):
    x += 1
    if x > n: x = 1
    return x

def decrement(x):
    x -= 1
    if x == 0: x = n
    return x

def decode(w, a, b, c):
    res = ''
    for x in w:
        if x.isalpha():
            idx = 26 - ((ord(x)-ord('A') +1 + a + b + c) % 26)
            res += chr(ord('A')-1+idx)
            if b % 3 == 0: a = increment(a)
            if c % 5 == 0: b = increment(b)
            c = increment(c)
        else:
            res += x
    return res

d = {}
for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            msg = decode("AMGINE", a, b, c)
            d[msg] = (a, b, c)

while True:
    w = input()
    if w == ".": break
    for msg in d:
        idx = w.find(msg)
        if idx >= 0:
            a, b, c = d[msg]
            while idx > 0:
                if w[idx].isalpha():
                    c = decrement(c)
                    if c % 5 == 0: b = decrement(b)
                    if b % 3 == 0: a = decrement(a)
                idx -= 1
            print(a, b, c)
            print(decode(w, a, b, c))
            break
```