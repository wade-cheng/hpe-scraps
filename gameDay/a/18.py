import sys
x = [line.strip() for line in sys.stdin]
conj = x[0]
x.pop(0)

if len(x) == 1:
    print(x[0])
elif len(x) == 2:
    print(f"{x[0]} {'and' if conj == 'AND' else 'or'} {x[1]}")
else:
    tempAns = ""
    for i, str in enumerate(x):
        tempAns += f"{str}, "
        if i == len(x) - 2:
            tempAns += 'and ' if conj == 'AND' else 'or '
    print(tempAns[:-2])