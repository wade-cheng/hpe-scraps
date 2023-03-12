import sys
x = [line.strip() for line in sys.stdin]
for a in x:
    if a=="0":
        break
    else:
        if int(a)%5==0 and int(a)%9==0:
            print(str(a) + " FIZZ FUZZ!")
        elif int(a)%5==0:
            print(str(a) + " FIZZ")
        elif int(a)%9==0:
            print(str(a) + " FUZZ")