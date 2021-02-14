# defining a cell

MAXROW = 9
MAXCOL = 10

src = [0, 0]
dest = [8, 9]

class cell:
    parent = [-1, -1]
    f = g = h = 0

def isvalid(row, col):
    if(row >= 0 and col >= 0) and (row < MAXROW and col < MAXCOL):
        return True
    else:
        return False

def is_unblocked(grid, row, col):
    if(grid[row][col] == 1):
        return  True
    else:
        return False

def is_destination(row, col):
    if(row == dest[0] and col == dest[1]):
        return True
    else:
        return False

def heuristic(row, col):
    return (dest[0] - row) + (dest[1] - col)

def print_path(parent):
    x = 8
    y = 9
    path = []
    for i in range(0, MAXROW):
        t = []
        for j in range(0, MAXCOL):
            t.append(0)
        path.append(t)

    flag = True
    while(flag):
        path[x][y] = 1
        x1 = x
        y1 = y
        x = parent[x1][y1].parent[0]
        y = parent[x1][y1].parent[1]
        if x == src[0] and y == src[1]:
            flag = False

    path[src[0]][src[1]] = 1

    for l in path:
        print(l)

def a_star_search(grid):

    result = False

    if(is_unblocked(grid, src[0], src[1]) == False or is_unblocked(grid, dest[0], dest[1]) == False):
        print("The source or the destinantion are blocked! ERROR!!")
        return


    parentGrid = []

    for i in range(0, MAXROW):
        t = []
        for j in range(0, MAXCOL):
            garbage = cell()
            t.append(garbage)
        parentGrid.append(t)

    parentGrid[src[0]][src[1]].parent = [src[0], src[1]]

    open = []
    close = []
    for i in range(0, MAXROW):
        t = []
        for j in range(0, MAXCOL):
            t.append(False)
        close.append(t)

    i = src[0]
    j = src[1]

    open.append([0, (i, j)])

    while(len(open) != 0):
        head = open[0]

        open.remove(head)
        i = head[1][0]
        j = head[1][1]

        close[i][j] = True

        # Checking successors
        # ----------NORTH----------
        if(isvalid(i - 1, j) == True):
            if(is_destination(i - 1, j) == True):
                temp = cell()
                temp.parent = [i, j]
                parentGrid[i - 1][j] = temp
                print_path(parentGrid)
                result = True
                return

            if(close[i - 1][j] == False and is_unblocked(grid, i - 1, j)):
                newG = parentGrid[i][j].g + 1
                newH = heuristic(i - 1, j)
                newF = newG + newH

                if(parentGrid[i - 1][j].f > newF or parentGrid[i - 1][j].f == 0):
                    temp = cell()
                    temp.parent = [i, j]
                    temp.f = newF
                    temp.g = newG
                    temp.h = newH

                    open.append([newF, [i - 1, j]])
                    parentGrid[i - 1][j] = temp


        # ----------SOUTH----------
        if(isvalid(i + 1, j) == True):
            if(is_destination(i + 1, j) == True):
                temp = cell()
                temp.parent = [i, j]
                parentGrid[i + 1][j] = temp
                print_path(parentGrid)
                result = True
                return

            if(close[i + 1][j] == False and is_unblocked(grid, i + 1, j)):
                newG = parentGrid[i][j].g + 1
                newH = heuristic(i + 1, j)
                newF = newG + newH

                if(parentGrid[i + 1][j].f > newF or parentGrid[i + 1][j].f == 0):
                    temp = cell()
                    temp.parent = [i, j]
                    temp.f = newF
                    temp.g = newG
                    temp.h = newH

                    open.append([newF, [i + 1, j]])
                    parentGrid[i + 1][j] = temp

        # ----------EAST----------
        if(isvalid(i, j + 1) == True):
            if(is_destination(i, j + 1) == True):
                temp = cell()
                temp.parent = [i, j]
                parentGrid[i][j + 1] = temp
                print_path(parentGrid)
                result = True
                return

            if(close[i][j + 1] == False and is_unblocked(grid, i, j + 1)):
                newG = parentGrid[i][j].g + 1
                newH = heuristic(i, j + 1)
                newF = newG + newH

                if(parentGrid[i][j + 1].f > newF or parentGrid[i][j + 1].f == 0):
                    temp = cell()
                    temp.parent = [i, j]
                    temp.f = newF
                    temp.g = newG
                    temp.h = newH

                    open.append([newF, [i, j + 1]])
                    parentGrid[i][j + 1] = temp

        # ----------WEST----------
        if(isvalid(i, j - 1) == True):
            if(is_destination(i, j - 1) == True):
                temp = cell()
                temp.parent = [i, j]
                parentGrid[i][j - 1] = temp
                print_path(parentGrid)
                result = True
                return

            if(close[i][j - 1] == False and is_unblocked(grid, i, j - 1)):
                newG = parentGrid[i][j].g + 1
                newH = heuristic(i, j - 1)
                newF = newG + newH

                if(parentGrid[i][j - 1].f > newF or parentGrid[i][j - 1].f == 0):
                    temp = cell()
                    temp.parent = [i, j]
                    temp.f = newF
                    temp.g = newG
                    temp.h = newH

                    open.append([newF, [i, j - 1]])
                    parentGrid[i][j - 1] = temp



    if(result == True):
        print("Failed to fint destination :- ")



grid = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
]

a_star_search(grid)









