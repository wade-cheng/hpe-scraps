import sys
import string
x = [line.strip() for line in sys.stdin][:-1]
maxDialSize = int(x[0])
x.pop(0)

charToInt = {
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":10,
    "K":11,
    "L":12,
    "M":13,
    "N":14,
    "O":15,
    "P":16,
    "Q":17,
    "R":18,
    "S":19,
    "T":20,
    "U":21,
    "V":22,
    "W":23,
    "X":24,
    "Y":25,
    "Z":26,
}

intToChar = {
    1:"A",
    2:"B",
    3:"C",
    4:"D",
    5:"E",
    6:"F",
    7:"G",
    8:"H",
    9:"I",
    10:"J",
    11:"K",
    12:"L",
    13:"M",
    14:"N",
    15:"O",
    16:"P",
    17:"Q",
    18:"R",
    19:"S",
    20:"T",
    21:"U",
    22:"V",
    23:"W",
    24:"X",
    25:"Y",
    26:"Z",
}

class Dial:
    def __init__(self, currn, size):
        self.currn = currn
        self.size = size
    def rotate(self):
        self.currn += 1
        if self.currn > self.size:
            self.currn = 1

def solve(c:str, dial1:Dial, dial2:Dial, dial3:Dial) -> str: # types string and Dial objs
    if c not in string.ascii_letters:
        raise Exception("asl;kdfjlsadkjf careful, code only works without these")
    else:
        temp1 = charToInt[c]
        sumX = temp1 + dial1.currn + dial2.currn + dial3.currn
        charAns = intToChar[26 - (sumX % 26)] # char ans here
        # now rotate
        if dial2.currn % 3 == 0:
            dial1.rotate()
        if dial3.currn % 5 == 0:
            dial2.rotate()
        dial3.rotate()
    return charAns

def findTempName(line):
    for diala in range(1,maxDialSize+1):
        for dialb in range(1, maxDialSize + 1):
            for dialc in range(1, maxDialSize + 1):
                dial1 = Dial(diala, maxDialSize)
                dial2 = Dial(dialb, maxDialSize)
                dial3 = Dial(dialc, maxDialSize)

                ans = ""
                correctDial: str = ""
                found = False
                for c in line:
                    if c not in string.ascii_letters:
                        ans += c
                    else:
                        returned = solve(c, dial1, dial2, dial3)
                        ans += returned
                        if "AMGINE" in ans:
                            found = True
                            correctDial = f"{diala} {dialb} {dialc}"
                if found:
                    return f"{correctDial}\n{ans}"

# print(x)
# exit()
for line in x:
    print(findTempName(line))
