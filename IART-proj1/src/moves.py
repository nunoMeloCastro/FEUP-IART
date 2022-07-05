def moveright(pos, maze):
    if((maze[pos[0]][pos[1]][3] != 1)):
        pos[1] += 1
        return 1
    return 0


def moveleft(pos, maze):
    if((maze[pos[0]][pos[1]][2] != 1)):
        pos[1] -= 1
        return 1
    return 0


def moveup(pos, maze):
    if((maze[pos[0]][pos[1]][0] != 1)):
        pos[0] -= 1
        return 1
    return 0


def movedown(pos, maze):
    if((maze[pos[0]][pos[1]][1] != 1)):
        pos[0] += 1
        return 1
    return 0

# checks which way to move


def move(seq, pos, goal, maze):

    if seq == []:
        return pos

    for j in range(0, round(len(maze)*2)):

        for i in seq:

            if i.upper() == 'L':
                moveleft(pos, maze)

            elif i.upper() == 'R':
                moveright(pos, maze)

            elif i.upper() == 'U':
                moveup(pos, maze)

            elif i.upper() == 'D':
                movedown(pos, maze)

            if pos == goal:
                return pos
    return pos
