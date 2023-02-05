"""
Wade and Kyle's scuffed bfs solution to Lights Out
"""

import copy
import sys
x = [[0 if char == "." else 1 for char in line.strip()] for line in sys.stdin]

if sum(map(sum, x)) == 0:
    print(0)  # PRINT ANS
    exit()

def getNewState(oldBoardState, clickI, clickJ):
    """boardState is 2d array of current state"""
    boardState = copy.deepcopy(oldBoardState)

    boardState[clickI][clickJ] = 1 if boardState[clickI][clickJ] == 0 else 0
    if clickI + 1 <= 4:
        boardState[clickI + 1][clickJ] = 1 if boardState[clickI + 1][clickJ] == 0 else 0
    if clickI - 1 >= 0:
        boardState[clickI - 1][clickJ] = 1 if boardState[clickI - 1][clickJ] == 0 else 0
    if clickJ + 1 <= 4:
        boardState[clickI][clickJ + 1] = 1 if boardState[clickI][clickJ + 1] == 0 else 0
    if clickJ - 1 >= 0:
        boardState[clickI][clickJ - 1] = 1 if boardState[clickI][clickJ - 1] == 0 else 0

    return boardState

possibleTiles = []
for i in range(5):
    for j in range(5):
        possibleTiles.append([i,j])

queue = [[copy.deepcopy(x),0]] # each item is [boardState (2d list), moves to get here]
boardStatesVisited = [copy.deepcopy(x)]  # list of 2d lists
while True:
    nextStateInQ = queue.pop(0)  # [boardState (2d list), moves to get here]
    for tile in possibleTiles:
        newState = getNewState(nextStateInQ[0], tile[0], tile[1])  # is a 2d list
        if sum(map(sum,newState)) == 0:  # check if done
            print(nextStateInQ[1]+1) # PRINT ANS
            exit()
        if newState not in boardStatesVisited:
            queue.append([newState,nextStateInQ[1]+1])
            boardStatesVisited.append(newState)