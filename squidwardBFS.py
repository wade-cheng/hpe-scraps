import sys
temp=[]
i=0
for line in sys.stdin:
    if(i==0):
        wid=int(line.strip())
    elif(i==1):
        length=int(line.strip())
    else:
        temp.append(line.strip())
    i+=1
grid = [list(line.strip()) for line in temp if line.strip()!=""]
#print(map)
obstacles = []
impossible = True

steps = [] #q
tracker = dict() #counts number of moves

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
idx = 0

for y, row in enumerate(grid):
    for x, pos in enumerate(row):
        if pos == 'T':
            Start = (x, y)
            steps.append((x,y))
            tracker[(x,y)] = idx
        elif pos == 'D':
            end = (x, y)
        elif pos == 'W':
            obstacles.append((x,y))

def next_moves(curr_x, curr_y):
    next_list = []

    for next in moves:
        next_x, next_y = curr_x + next[0], curr_y + next[1]
        #inside board
        if not (next_x < 0 or next_y < 0 or next_y >= len(grid) or next_x >= len(grid[0]) or (next_x, next_y) in obstacles or (next_x, next_y) in steps):
            next_list.append((next_x, next_y))

    return next_list


while idx < len(steps):
     curr_x, curr_y = steps[idx]
     idx += 1

     if (curr_x, curr_y) == end:
         print(tracker[(curr_x, curr_y)])
         impossible = False
         break

     for next_x, next_y in next_moves(curr_x, curr_y):
         steps.append((next_x, next_y))
         tracker[(next_x, next_y)] = tracker[(curr_x, curr_y)] + 1


