# test case arrays
x = [
    "123456789",
    "abcdefghi",
    "!@#$%^&*(",
]

y = [
    "qaz",
    "wsx",
    "edc",
    "rfv",
]

z = [
    "*    ",
    "*****",
]

# code (NOTE: RECTANGULAR ARRAYS ONLY)
unflippedArray = z
finalArray = [""] * len(unflippedArray[0])  # [[]] * int  # if need actual arrays instead of str

# TODO these two need to be taken out for clockwise. left in, array is spun counterclockwise
# unflippedArray = [line[::-1] for line in unflippedArray]

for newI in range(len(unflippedArray[0])):
    for newJ in range(len(unflippedArray) - 1, -1, -1):
        finalArray[newI] += unflippedArray[newJ][newI]

# TODO these two need to be taken out for clockwise. left in, array is spun counterclockwise
# finalArray = [line[::-1] for line in finalArray]

# print array
for i in finalArray:
    print(i)
