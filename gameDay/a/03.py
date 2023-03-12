import sys
x = [line.strip() for line in sys.stdin]
i = int(x[0])
cap = int(x[1])
rate = float(x[2])
years = int(x[3])
temp = i*(1+rate)*years
temp1 = str(temp)[: str(temp).index('.')]
print("At the current rate of growth there will be " + temp1 + " ponies in " + str(years) + " years.")
if(int(temp1)<=cap):
    print("Celestia won't need to add space yet!")
else:
    print("Celestia will need to add space for at least " + str((int(temp1)-cap)) + " ponies!")