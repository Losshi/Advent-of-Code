# Problem - Part 1
def distinctPathPositions(data,start,rows,cols,obstr):
    data = [list(row) for row in data]
    isObj = len(obstr)
    if isObj != 0:
        data[obstr[0]][obstr[1]] = '#'
    positions = set()
    x, y = start
    paths = ((-1,0),(0,1),(1,0),(0,-1))
    d = 0
    while x >= 0 and x < rows and y >= 0 and y < cols:
        if (x, y, d) in positions and isObj != 0:
            return True
        if data[x][y] == "#":
            x -= paths[d][0]
            y -= paths[d][1]
            d = (d + 1) % 4 
        else:
            if isObj != 0:
                positions.add((x,y,d))
            else:
                positions.add((x,y))
        x += paths[d][0]
        y += paths[d][1]
    if isObj != 0:
        return False
    return positions

# Problem - Part 2
def findPositionsForLoop(data, start, rows, cols):
    count = 0
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == '.':  
                if distinctPathPositions(data, start, rows, cols, (i, j)):
                    count += 1
    return count

with open("../inputs/Input_Day_06.txt","r") as file:
    data = file.readlines()
    rows = len(data)
    cols = len(data[0].strip())
    start = ()
    for i in range(rows):
        s = data[i]
        if s.find("^") != -1:
            start = (i,s.find("^"))
            break
    
    # Problem - Part 1
    positions = distinctPathPositions(data,start,rows,cols,())
    print(len(positions))

    # Problem - Part 2
    print(findPositionsForLoop(data,start,rows,cols))


# Sample Input:
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...

# Sample Output:
# 41
# 6