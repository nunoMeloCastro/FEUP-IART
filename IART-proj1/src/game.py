from ctypes.wintypes import RGB
import pygame
from time import sleep
from interface import *
from ai import *
from moves import *
from utils import *
import os


def checkOption(pos):

    x = pos[0]
    y = pos[1]

    if x >= OPTIONS_X and x <= OPTIONS_X + OP_WIDTH:
        if y >= OPTION1_Y and y <= OPTION1_Y + OP_HEIGHT:
            return 1
        elif y >= OPTION2_Y and y <= OPTION2_Y + OP_HEIGHT:
            return 2
        elif y >= OPTION3_Y and y <= OPTION3_Y + OP_HEIGHT:
            return 3
        else:
            return 0


def chooseMaze(window, font):

    drawMazeOptions(window, font)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                op = mazeCheckOption(pos)

                if op >= 1 and op <= NUMBER_OF_MAZES:
                    mazeName = "p" + str(op)
                    return mazeName

            pygame.display.flip()


def mazeOptionsOtimize(y, num):

    curY = MAZESOP_Y
    count = 1
    for i in range(int(NUMBER_OF_MAZES / 2)):
        if y >= curY and y <= curY + MAZEOP_HEIGHT:
            #print(num + count)
            break
        count += 1
        curY += MAZESOP_YDIST

    return num + count


def mazeCheckOption(pos):

    x = pos[0]
    y = pos[1]
    num = 0
    if x >= MAZESOP_X and x <= MAZESOP_X + MAZEOP_WIDTH:
        number = mazeOptionsOtimize(y, num)
    elif x >= MAZESOP_X + MAZESOP_XDIST and x <= MAZESOP_X + MAZESOP_XDIST + MAZEOP_WIDTH:
        num = 10
        number = mazeOptionsOtimize(y, num)

    return number


def chooseSearch(window, font):

    drawSearchOptions(window, font)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                op = searchCheckOption(pos)

                if op == 1:
                    return "bfs"
                elif op == 2:
                    return "dfs"
                elif op == 3:
                    return "greedy"
                elif op == 4:
                    return "astar"

            pygame.display.flip()


def searchCheckOption(pos):

    x = pos[0]
    y = pos[1]

    if x >= OPTIONS_X and x <= OPTIONS_X + OP_WIDTH:
        if y >= SEARCH_OPTION1_Y and y <= SEARCH_OPTION1_Y + OP_HEIGHT:
            return 1
        if y >= SEARCH_OPTION2_Y and y <= SEARCH_OPTION2_Y + OP_HEIGHT:
            return 2
        if y >= SEARCH_OPTION3_Y and y <= SEARCH_OPTION3_Y + OP_HEIGHT:
            return 3
        if y >= SEARCH_OPTION4_Y and y <= SEARCH_OPTION4_Y + OP_HEIGHT:
            return 4

    return 0


def chooseHeuristic(window, font):

    drawHeuristicOptions(window, font)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                op = heuristicCheckOption(pos)

                if op == 1:
                    return "man"
                elif op == 2:
                    return "euc"
                elif op == 3:
                    return "cheby"

            pygame.display.flip()


def heuristicCheckOption(pos):

    x = pos[0]
    y = pos[1]

    if x >= HEURISTIC_OPTIONS_X and x <= HEURISTIC_OPTIONS_X + HEURISTIC_OP_WIDTH:
        if y >= OPTION1_Y and y <= OPTION1_Y + OP_HEIGHT:
            return 1
        elif y >= OPTION2_Y and y <= OPTION2_Y + OP_HEIGHT:
            return 2
        elif y >= OPTION3_Y and y <= OPTION3_Y + OP_HEIGHT:
            return 3
        else:
            return 0


def humanMode(window, font):
    mazeName = chooseMaze(window, font)
    if mazeName == 0:
        return
    maze = globals()[mazeName]

    mazeSolSizeName = mazeName + "SolSize"
    mazeSolSize = globals()[mazeSolSizeName]
    bestseq = greedy(start, goal, maze, mazeSolSize, "euc")
    seq = []

    sleep(1)

    agentPos = start
    solving = True

    while(solving):
        hintVal = 0
        rectSizes = initMaze(window, maze, goal)
        pygame.display.flip()
        while(1):
            # os.system('cls') #used to clear terminal
            seq = input(
                'Choose movement direction: \n L => Left \n R => Right \n U => Up \n D => Down \n H => Hint \n Q => Quit \n ->')
            if seq.upper() == 'H':
                print('Hint', hintVal, ': ', bestseq[hintVal], "\n")
                sleep(2)
                if(hintVal+1 < len(bestseq)):
                    hintVal += 1
                else:
                    print("Solution: ", "".join(bestseq))
            elif seq.upper() == 'Q':
                print('BETTER LUCK NEXT TRY!!!\n')
                return
            else:
                break
        counter = 0
        while(counter < round(len(maze)*2) and solving):
            counter += 1
            for i in seq:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                sleep(0.5)
                if agentPos == goal:
                    solving = False
                    break

                oldPos = agentPos
                if i == "R" or i == "r":
                    agentPos = getRight(agentPos, maze)
                elif i == "L" or i == "l":
                    agentPos = getLeft(agentPos, maze)
                elif i == "D" or i == "d":
                    agentPos = getDown(agentPos, maze)
                elif i == "U" or i == "u":
                    agentPos = getUp(agentPos, maze)

                if oldPos != agentPos and counter != 0:
                    # remove agent
                    drawAgent(window, oldPos[0], oldPos[1],
                              rectSizes[0], rectSizes[1], GREEN)
                drawAgent(window, agentPos[0], agentPos[1],
                          rectSizes[0], rectSizes[1], BLUE)
                pygame.display.flip()
        if(not solving):
            print("\n!!Got it!!")
            print("Here is the best answer: ", bestseq)
            return
        else:
            repeatTry = input("Sorry, want to try again? (y/n)")
            drawAgent(window, agentPos[0], agentPos[1],
                      rectSizes[0], rectSizes[1], WHITE)
            agentPos = [4, 0]
            if(repeatTry.upper() == 'Y'):
                continue
            else:
                print("see you next time")
                return


def aiMode(window, font):

    mazeName = chooseMaze(window, font)
    if mazeName == 0:
        return
    maze = globals()[mazeName]
    method = chooseSearch(window, font)

    mazeSolSizeName = mazeName + "SolSize"
    mazeSolSize = globals()[mazeSolSizeName]

    if method == "bfs":
        seq = bfs(start, goal, maze)

    elif method == "dfs":
        seq = dfs(start, goal, maze, mazeSolSize)

    elif method == "greedy":
        heuristic = chooseHeuristic(window, font)
        seq = greedy(start, goal, maze, mazeSolSize, heuristic)

    elif method == "astar":
        heuristic = chooseHeuristic(window, font)
        seq = aStar(start, goal, maze, mazeSolSize, heuristic)

    else:
        return

    rectSizes = initMaze(window, maze, goal)
    pygame.display.flip()
    sleep(1)

    agentPos = start
    solving = True
    print("Sequence: ", seq)

    while solving == True:
        for i in seq:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            print("Next move: ",i)
            sleep(0.5)
            if agentPos == goal:
                solving = False
                break

            oldPos = agentPos
            if i == "R":
                agentPos = getRight(agentPos, maze)
            elif i == "L":
                agentPos = getLeft(agentPos, maze)
            elif i == "D":
                agentPos = getDown(agentPos, maze)
            elif i == "U":
                agentPos = getUp(agentPos, maze)

            if oldPos != agentPos:
                # remove agent
                drawAgent(window, oldPos[0], oldPos[1],
                          rectSizes[0], rectSizes[1], GREEN)
                drawAgent(window, agentPos[0], agentPos[1],
                          rectSizes[0], rectSizes[1], BLUE)
                pygame.display.flip()


def main():

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Python Maze Generator")
    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.SysFont(FONT, 30)

    width = mazeSize*BLOCK
    height = mazeSize*BLOCK

    if width > 600:
        width = 600
    if height > 600:
        height = 600

    window = pygame.display.set_mode([width, height])

    drawMenu(window, font)

    running = True
    menu = True

    while running:
        clock.tick(FPS)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                op = checkOption(pos)
                if op == 1:
                    humanMode(window, font)
                    #print("end human mode")
                elif op == 2:
                    aiMode(window, font)
                elif op == 3:
                    exit()

        # Flip the display
        pygame.display.flip()

    pygame.quit()


main()
