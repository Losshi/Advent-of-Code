# Problem - Part 1
def isIncreasingByLimit(report):
    for i in range(len(report)-1):
        if report[i] >= report[i+1]:
            return False
        levelDiff = report[i+1] - report[i]
        if levelDiff < 1 or levelDiff > 3:
            return False
    return True
    
def isDecreasingByLimit(report):
    for i in range(len(report)-1):
        if report[i] <= report[i+1]:
            return False
        levelDiff = report[i] - report[i+1]
        if levelDiff < 1 or levelDiff > 3:
            return False
    return True

# Problem - Part 2
def isProblemDamped(report):
    levels = len(report)
    for level in range(levels):
        subreport = report[0:level] + report[level+1:levels]
        if isIncreasingByLimit(subreport) or isDecreasingByLimit(subreport):
            return True
    return False

with open('../inputs/Input_Day_02.txt','r') as file:
    data = file.readlines()
    safe = 0
    tolSafe = 0
    for line in data:
        report = [int(level) for level in line.split()]
        if isIncreasingByLimit(report) or isDecreasingByLimit(report):
            safe += 1
            tolSafe += 1
        elif isProblemDamped(report):
            tolSafe += 1
    print(safe)         # Problem - Part 1 answer 
    print(tolSafe)      # Problem - Part 2 answer
    

# Sample Input:
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9

# Sample Output: 
# 2
# 4