from moves import *
from utils import *
import math
from time import sleep

costBFS = 0
costDFS = 0
costGreedy = 0
costAstar = 0


def getCostBfs():
    global costBFS
    return costBFS


def getCostDfs():
    global costDFS
    return costBFS


def getCostGreedy():
    global costGreedy
    return costGreedy


def getCostAstar():
    global costAstar
    return costAstar

# manhattan distance heuristic calculator


def manDist(robotPos, finalPos):
    h = abs(robotPos[0] - finalPos[0]) + abs(robotPos[1] - finalPos[1])
    return h

# euclidean distance heuristic calculator


def eucDist(robotPos, finalPos):
    h = math.dist(robotPos, finalPos)
    return h

# Chebyshev distance heuristic calculator


def chebyDist(robotPos, finalPos):
    h = max(abs(robotPos[0] - finalPos[0]), abs(robotPos[1] - finalPos[1]))
    return h


def dfs(start, goal, maze, sizeOfAnswer, seq=None, res=None, visited=None, limit=None):
    global costDFS
    costDFS += 1
    if seq is None:
        seq = []

    if visited is None:
        visited = []

    if limit is None:
        limit = 0

    if res is None:
        res = []

    if limit <= sizeOfAnswer and res == []:

        if seq != []:
            visited.append([seq])

        aux = [start[0], start[1]]

        if goal == move(seq, aux, goal, maze) and len(seq) == sizeOfAnswer:

            res = seq
            return res

        # visualizeCode(seq,0.5) #uncomment to visualize code

        for movDir in ["U", "R", "L", "D"]:
            newSeq = list(seq)
            newSeq.append(movDir)
            if newSeq not in visited:
                res = dfs(start, goal, maze, sizeOfAnswer,
                          newSeq, res, visited, (limit+1))
        return res
    return res


def bfs(start, goal, maze):
    global costBFS
    queue = []
    queue.append(["L"])
    queue.append(["R"])
    queue.append(["U"])
    queue.append(["D"])
    count = 0
    while queue:
        count += 1
        seq = queue.pop(0)
        aux = [start[0], start[1]]
        # unprint to visualize search path
        # visualizeCode(seq,0.5) #uncomment to visualize code

        if goal == move(seq, aux, goal, maze):

            costBFS = count

            return seq

        for movDir in ["L", "R", "U", "D"]:
            newSeq = list(seq)
            newSeq.append(movDir)
            queue.append(newSeq)


def greedy(start, goal, maze, sizeOfAnswer, heuristic):
    global costGreedy
    queue = []
    queue.append(setUp("L", start, goal, maze, heuristic))
    queue.append(setUp("R", start, goal, maze, heuristic))
    queue.append(setUp("U", start, goal, maze, heuristic))
    queue.append(setUp("D", start, goal, maze, heuristic))
    count = 0

    # by storing the value in the queue we dont need to re-search the last position of each value each time
    # time saved from 0.8s -> 0.004s
    while queue:
        bestHeuristic = 999.0
        count += 1
        for i in range(len(queue)):
            if(queue[i][1] < bestHeuristic):
                bestVal = queue[i]
                bestHeuristic = queue[i][1]

        queue.remove(bestVal)

        # visualizeCode(bestVal[0],0.5) #uncomment to visualize code

        # checks depth
        if goal == bestVal[2]:

            costGreedy = count

            return bestVal[0]

        if(len(bestVal[0]) < sizeOfAnswer):
            for movDir in "LDUR":
                newSeq = setUp(bestVal[0]+movDir, start, goal, maze, heuristic)
                queue.append(newSeq)


def aStar(start, goal, maze, sizeOfAnswer, heuristic):
    global costAstar
    queue = []
    queue.append(setUp("L", start, goal, maze, heuristic))
    queue.append(setUp("R", start, goal, maze, heuristic))
    queue.append(setUp("U", start, goal, maze, heuristic))
    queue.append(setUp("D", start, goal, maze, heuristic))
    count = 0

    # by storing the value in the queue we dont need to re-search the last position of each value each time
    # time saved from 0.8s -> 0.004s
    while queue:
        bestHeuristic = 999.0
        for i in range(len(queue)):
            if(queue[i][1] <= bestHeuristic):
                if(queue[i][1] == bestHeuristic and len(queue[i][0]) > len(bestVal[0])):
                    continue
                else:
                    bestVal = queue[i]
                    bestHeuristic = queue[i][1]
        count += 1

        queue.remove(bestVal)

       # visualizeCode(bestVal[0],0.5) #uncomment to visualize code

        # checks depth
        if goal == bestVal[2]:
            costAstar = count
            return bestVal[0]

        if(len(bestVal[0]) < sizeOfAnswer):
            for movDir in "LDUR":
                newSeq = setUp(bestVal[0]+movDir, start, goal, maze, heuristic)
                queue.append(newSeq)


# function to store essencial values for A* and Greedy
def setUp(seq, start, goal, maze, heuristic):
    aux = [start[0], start[1]]
    # get last position achievable with that sequence
    pos = move(seq, aux, goal, maze)
    if heuristic == "man":
        return [seq, manDist(pos, goal), pos]
    elif heuristic == "cheby":
        return [seq, chebyDist(pos, goal), pos]
    elif heuristic == "euc":
        return [seq, eucDist(pos, goal), pos]


def visualizeCode(seq, sleepTime):
    sleep(sleepTime)
    print(seq)
