import sys
x = [line.strip() for line in sys.stdin][:-1]
fib=[0,1,1]
for i in range(37):
    fib.append(fib[i]+fib[i+1]+fib[i+2])
for i in x:
    temp=i.split(" ")
    print(fib[int(temp[0])]-fib[int(temp[1])])