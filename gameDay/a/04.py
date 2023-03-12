import sys
x = [line.strip() for line in sys.stdin]
imp=x[0]
word=x[1]
ind = word.index(imp)
print(imp + " is at index: " + str(ind))