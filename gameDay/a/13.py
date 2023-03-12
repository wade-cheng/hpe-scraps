import sys
x = [line.strip() for line in sys.stdin][:-1]
for i in x:
    if i.count("-")==2:
        print("xxx-xx" + i[6:])
    else:
        print("xxxx-xxxx-xxxx" + i[14:])