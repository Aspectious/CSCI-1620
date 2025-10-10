
def mazeSearch(grid, x, y):
    maze = grid
    pos = [x,y]
    tileatpos = maze[pos[0],pos[1]]
    neighbortiles = []
    if (tileatpos == 2): 
        return True
    # Check left tile
    if (not pos[0] == 0):
        tile = maze[pos[0]-1,pos[1]]
        neighbortiles.append([-1,0,tile])
    else:
        neighbortiles.append([-1,0,1])
    # Check top tile
    if (not pos[1] == 0):
        tile = maze[pos[0],pos[1]-1]
        neighbortiles.append([0,-1,tile])
    else:
        neighbortiles.append([0,-1,1])

    # Check right tile
    if (not pos[0] == len(maze)-1):
        tile = maze[pos[0]+1,pos[1]]
        neighbortiles.append([1,0,tile])
    else:
        neighbortiles.append([1,0,1])

    # Check bottom tile
    if (not pos[1] == len(maze)-1):
        tile = maze[pos[0],pos[1]+1]
        neighbortiles.append([0,1,tile])
    else:
        neighbortiles.append([0,1,1])



    #Recursive Algorithm
    numoptions = 0
    foundend = False
    solutionpath = []
    for sel in neighbortiles:
        if (sel[2] == 2):
            foundend = True
            [sel[0],sel[1]]
        elif (sel[2] == 0):



def mainMaze():
    grid = [[0,0,0,0,0,1],
            [1,1,0,0,0,1],
            [0,0,0,1,0,0],
            [0,1,1,0,0,1],
            [0,1,0,0,1,0],
            [0,1,0,0,0,2]]
    print(mazeSearch(grid, 0, 0))


mainMaze()
