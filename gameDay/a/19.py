import sys
x = [line.strip() for line in sys.stdin]
word = x[0]
length = int(x[1])
i=0
j=0
mvRight = True
mvDown = False
mvLeft = False
mvUp = False

locs = []

locs.append((word[0],i,j))
x = 1
while True:
    char = word[x]
    x += 1
    if x > len(word) - 1:
        x = 0
    if not mvDown:
        j += 1
        # add to arr
        if j > length - 1:
            j -= 1
            i += 1
            mvDown = True
        locs.append((char, i, j))
    elif not mvLeft:
        i += 1
        # add to arr
        if i > length - 1:
            i -= 1
            j -= 1
            mvLeft = True
        locs.append((char, i, j))
    elif not mvUp:
        j -= 1
        # add to arr
        if j == -1:
            j = 0
            i -= 1
            mvUp = True
        locs.append((char, i, j))
    else: # move up
        i -= 1
        # add to arr
        locs.append((char, i, j))
        if i == 1:
            break

# print(locs)
ans = []
for eye in range(length):
    temp=""
    for jay in range(length):
        found = False
        for ii, loc in enumerate(locs):
            if loc[1] == eye and loc[2] == jay:
                temp += loc[0]
                found = True
        if not found:
            temp += " "
    ans.append(temp)
print("\n".join(ans).replace(".", ""))