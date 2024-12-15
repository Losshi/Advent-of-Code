import re

def multiplyInstructions(matches):
    productSum = 0 
    for inst in matches:
        a = int(inst[1])
        b = int(inst[2])
        productSum += (a*b)
    return productSum

with open('../inputs/Input_Day_03.txt','r') as file:
    data = file.readlines()

    # Problem - Part 1
    matches = []
    for s in data:
        pattern = r'(mul\((\d{1,3}),(\d{1,3})\))'
        matches.extend(re.findall(pattern,s))
    print(multiplyInstructions(matches))

    # Problem - Part 2
    corruptStr = ""
    for s in data:
        corruptStr += s
    dont = corruptStr.split("don't()")
    dontMatches = []
    for i in range(len(dont)):
        pattern = r'(mul\((\d{1,3}),(\d{1,3})\))'
        if i == 0:
            dontMatches.extend(re.findall(pattern,dont[i]))
        elif dont[i].find("do()") != -1:
            dontMatches.extend(re.findall(pattern,dont[i][dont[i].find("do()"):]))
    print(multiplyInstructions(dontMatches))


# Sample Input:
# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

# Sample Output:
# 161
# 48