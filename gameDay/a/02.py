import sys
x = [line.strip() for line in sys.stdin]
for num in x:
    if int(num)%4==0:
        print(num +"/4 = " + str(int(num)//4))
