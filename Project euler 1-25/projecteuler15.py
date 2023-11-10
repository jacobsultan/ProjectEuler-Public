import time
currtime = time.time()

grid = []
def canfill(x,y,board):
    if board[y][x] != 0:
        return False
    elif y == 20:
        if x >= 20:
            return False
        elif board[20][x + 1] != 0:
            return True
        else:
            return False
    elif x == 20:
        if y >= 20:
            return False
        elif board[20][y + 1] == 0:
            return False
        else:
            return True
    else:
        if board[y + 1][x] == 0 or board[y][x+1] == 0 :
            return False
        else:
            return True




for j in range(21):
    lev = []
    for i in range(21):
        lev.append(0)
    grid.append(lev)
grid[20][20] = 1

while(grid[0][0] == 0):
    stary = 0
    starx = 0
    done = False
    while(not done):
        if canfill(starx,stary,grid):
            if starx == 20:
                grid[stary][starx] = grid[stary + 1][starx]
            elif stary == 20:
                grid[stary][starx] = grid[stary][starx + 1]
            else:
                grid[stary][starx] = grid[stary][starx + 1] + grid[stary + 1][starx]
            done = True
        else:
            starx += 1
            if starx == 21:
                stary += 1
                starx = 0 

print(grid[0][0])
print(time.time() - currtime)



    
            




            