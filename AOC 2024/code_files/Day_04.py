# Problem - Part 1
def reverseHorizontalOccurences(data,s):
    rh = 0
    for line in data:
        rh += line[::-1].count(s)
    return rh
    
def horizontalOccurences(data,s):
    h = 0
    for line in data:
        h += line.count(s)
    h += reverseHorizontalOccurences(data,s)
    return h
    
def verticalOccurences(data,s):
    v = 0
    vdata = []
    for i in range(len(data[0].strip())):
        vline = ''
        for j in range(len(data)):
            vline += data[j][i]
        vdata.append(vline)
    v += horizontalOccurences(vdata,s)
    return v
    
def searchDiagonalWord(data,i,j,s):
    match = 0
    n = len(data)
    m = len(data[0].strip())
    if data[i][j] != s[0]:
        return match
    traversal = len(s)
    direction = [(1,1),(1,-1),(-1,1),(-1,-1)]
    for d in direction:
        cx,cy = i + d[0] , j + d[1]
        k = 1 
        while k < traversal:
            if cx >= n or cx < 0 or cy >= m or cy < 0:
                break
            if data[cx][cy] != s[k]:
                break 
            cx += d[0]
            cy += d[1] 
            k += 1 
        if k == traversal:
            match += 1
    return match

def diagonalOccurences(data,s):
    diag = 0
    for i in range(len(data)):
        for j in range(len(data[0].strip())):
            diag += searchDiagonalWord(data,i,j,s)
    return diag

# Problem - Part 2
def isXShapedMAS(data,i,j,s):
    d = [(1,1),(-1,-1),(-1,1),(1,-1)]
    cross1 = data[i+d[0][0]][j+d[0][1]] + 'A' + data[i+d[1][0]][j+d[1][1]]
    cross2 = data[i+d[2][0]][j+d[2][1]] + 'A' + data[i+d[3][0]][j+d[3][1]]
    if (cross1 == s or cross1[::-1] == s) and (cross2 == s or cross2[::-1] == s):
        return True
    return False  

def XWordOccurences(data,s):
    xc = 0
    for i in range(1,len(data)-1):
        for j in range(1,len(data[0].strip())-1):
                if data[i][j] == 'A' and isXShapedMAS(data,i,j,s):
                    xc += 1
    return xc
    
with open("../inputs/Input_Day_04.txt","r") as file:
    data = file.readlines()

    # Problem - Part 1
    s = "XMAS"
    xmasTimes = 0
    xmasTimes += horizontalOccurences(data,s)
    xmasTimes += verticalOccurences(data,s)
    xmasTimes += diagonalOccurences(data,s)
    print(xmasTimes)

    # Problem - Part 2
    s = "MAS"
    masTimes = 0
    masTimes += XWordOccurences(data,s)
    print(masTimes)
    

# Sample input:
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX

# Sample Output:
# 18
# 9