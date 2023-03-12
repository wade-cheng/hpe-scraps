### CodeWars XXVI - 23 - AutoWrong

### Observation

* Line 1 (the sentence to correct) seems to be always in *lowercase*.
* Line 5 contains a key-value pair indicating what set of letters can potentially be replaced with, for example, `'Q:W,S,A'` indicates that a letter `'Q'` can be substituted by a letter `'W'`, `'S'`, or `'A'`.
* Key observation, each word on Line 1 will only have at most 1 letter to be substituted.

### The Idea
We likely can skip Line 2 through 4 (the keyboard layout), this is just noise in the input, but Line 5 needs to be tokenized like this:

* First, split by `';'` to get us a list of info like `'Q:W,S,A'`.
* For each of the info, turn it to lower case for easier comparison, and split by `':'`, this will give you a letter `L` on the left side of `':'` and then a comma-separated letters which can potentially substitute `L`.

Then store these substitution rules to a dictionary.  So now for each letter, we have the info of what it can be substituted with.

```python
line = input()
for _ in range(3): input()
d = {}
for sub_info in input().split(";"):
    key, letters = sub_info.lower().split(":")
    d[key] = letters.split(",")
```

Continue to parse the input to build our vocabulary list.  For an easier lookup, we want to use a set to store the valid words in our vocabulary.

```python
vocab = set()
while True:
    w = input()
    if w == 'ZZZZZ': break
    vocab.add(w)
```

Now, we can just examine each word on the sentence to correct, and for each one of them we apply a mapping function to convert it to a correct word in our vocabulary.  The mapping function accepts an argument, the word to examine, and it simply does:

* If this word is already correct (i.e., already in the vocabulary), return it right away.
* If this word is not in our vocabulary, then check every letter of this word and try to substitute it according to the substitution rules (the dictionary we maintained). Return the new word after substitution that is part of our vocabulary.
* If no matches found, then just return the original word.

```python
def correct(w):
    if w in vocab: return w
    for i, x in enumerate(w):
        for y in d[x]:
            ww = w[:i] + y + w[i+1:]
            if ww in vocab: return ww
    return w

print(' '.join(map(correct, line.split(" "))))
```
