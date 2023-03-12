# lookup = {
#     'A':1,
#     'B':2,
#     'C':3,
#     'D':4,
#     'E':5,
#     'F':6,
#     'G':7,
#     'H':8,
#     'I':9,
#     'J':10,
#     'K':11,
#     'L':12,
#     'M':13,
#     'N':14,
#     'O':15,
#     'P':16,
#     'Q':17,
#     'R':18,
#     'S':19,
#     'T':20,
#     'U':21,
#     'V':22,
#     'W':23,
#     'X':24,
#     'Y':25,
#     'Z':26,
# }
import sys
x = [line.strip() for line in sys.stdin][:-1]
rep1=x[0][0].lower()
rep2=x[0][2].lower()
x.pop(0)
words=[]
for i in x:
    temp = i.lower().replace(rep1,rep2)
    temp2=temp.replace(rep2,rep1)
    words.append(temp2)
print(words)