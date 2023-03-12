import sys
x = [line.strip() for line in sys.stdin]
num = int(x[0])
orig = num
yes=[]
arr=[512,256,128,64,32,16,8,4,2,1]

for i in arr:
    if num>=i:
        print(str(i)+"=1")
        num-=i
        yes.append(i)

    else:
        print(str(i)+"=0")

curr=yes[0]
yes.pop(0)
for x in range(len(yes)):
    print(str(curr) + "+" + str(yes[x])+" = " + str(curr+yes[x]))
    curr+=yes[x]
print(str(orig) + " = " +str(bin(orig)[2:]))