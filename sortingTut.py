x = [
    [1,"b"],
    [3,"b"],
    [2,"c"],
    [0,"a"]
]

# most important sort (the one performed first) listed first in the tuple
x.sort(key=lambda y: (
    y[1],
    y[0],
))

print(x)
