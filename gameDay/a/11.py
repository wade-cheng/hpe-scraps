import sys
x = [line.strip() for line in sys.stdin]
kids = int(x[0])
full=kids//4
part=kids%4
if full==1 and part ==1:
    print("1 full car, 1 partial car")
elif full==1:
    if part>0:
        print("1 full car, 1 partial car")
    else:
        print("1 full car")
elif part==1:
    if full> 0:
        print(str(full) + " full cars, 1 partial car")
    else:
        print("1 partial car")
else:
    if part>0 and full>0:
        print(str(full)+ " full cars, 1 partial car")
    elif full>0:
        print(str(full) + " full cars")
    else:
        print("1 partial car")
