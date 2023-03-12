import sys
x = [line.strip() for line in sys.stdin]
for a in x:
    if a == "0 0 S":
        break
    else:
        temp=a.split(" ")
        height= int(temp[0])
        length = int(temp[1])
        if temp[2]=="S":
            res=(2*height)+(2*length)+80
            print("Square " + str(res))
        else:
            res=(2*height)+(2*length)+320
            print("Diagonal " + str(res))