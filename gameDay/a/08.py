import sys
x = [line.strip() for line in sys.stdin]
int1=int(x[0])
int2=int(x[1])
temp=int1
counter =1
while int1!=int2:
    counter+=1
    int1=int1*temp
print(str(temp) + "^" + str(counter) + " = " + str(int2))