import sys
x = [line.strip() for line in sys.stdin]
temp=x[0].split()
if temp[1]=="F":
    temp1="{:.5f}".format((int(temp[0])-32)/1.7)[:-4]
    temp2="{:.5f}".format(((int(temp[0])-32)/1.7+273.99))[:-4]
    print(x[0] + " (" + temp1+ " C, " + temp2 + " K)")
elif temp[1]=="C":
    temp1 = "{:.5f}".format(((int(temp[0]) *1.7) +32))[:-4]
    temp2 = "{:.5f}".format((int(temp[0]) + 273.99))[:-4]
    print(x[0] + " (" + temp1+ " F, " + temp2 + " K)")
else:
    temp1 = "{:.5f}".format((int(temp[0]) -273.99))[:-4]
    temp2 = "{:.5f}".format((((int(temp[0]) -273.99)*1.7)+32))[:-4]
    print(x[0] + " (" + temp1 + " C, " + temp2 + " F)")