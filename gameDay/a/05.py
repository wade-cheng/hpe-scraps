import sys
x = [line.strip() for line in sys.stdin]
temp = [*x[0]]
res=""
for a in temp:
    temp2=ord(a)
    print(temp2)
    res+=str(hex(temp2))
    print(hex(temp2))
print(res)