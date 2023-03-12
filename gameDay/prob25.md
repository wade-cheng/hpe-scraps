### CodeWars XXVI - 25 - Trailers

### Observation

* We need to traverse the given directory, and we need to traverse deep on the child subdirectories as well as needed.
* For the most part we need to keep traversing each found directory until we see a directory name which matches the searched name.
* Based on the expected output, looks like we will need to output the directory separator using *Windows* separator (`'\'`).

### The Idea
It's usually more intuitive to do a recursive traversal.  During the traversal, we will pass the base directory name and the searched name.  Everytime we see another directory on one level, we will either:
* traverse further recursively, if that directory name is not the one we are searching for, or
* stop the traversal if we found the searched directory name, upon which, we will just look for one more directory `'trailers'`, and if it exists, check further if it contains a file name with `'.m2ts'` extension.

```python
import os

def find_trailer(dir_name, search_name):
    for name in os.listdir(dir_name):
        joined = os.path.join(dir_name, name)
        if os.path.isdir(joined):
            if name == search_name:
                trailer_dir = os.path.join(joined, 'trailers')
                if os.path.exists(trailer_dir) and os.path.isdir(trailer_dir):
                    for trailer in os.listdir(trailer_dir):
                        if trailer.endswith(".m2ts"): return trailer_dir + "/" + trailer
                    return ""
                else:
                    return ""
            else:
                res = find_trailer(os.path.join(dir_name, name), search_name)
                if res: return res
    return ""

dir_name = f"files/{input()}/"

while True:
    name = input()
    if name == "END": break
    res = find_trailer(dir_name, name)
    if res:
        print(name, "trailer was found at:", res[len(dir_name):].replace('/', '\\'))
    else:
        print(name, "trailer missing")
```