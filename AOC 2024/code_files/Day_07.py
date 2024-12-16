from itertools import product

def computeEquation(operands,operators):
    result = operands[0]
    for i in range(1,len(operands)):
        op = operators[i-1]
        # Problem - Part 1
        if op == '+':
            result += operands[i]
        elif op == '*':
            result *= operands[i]
        # Problem - Part 1
        elif op == '||':
            result = int(str(result)+str(operands[i]))
    return result

def calculateCalibrationResult(part):
    calibrated_result = 0
    combinations = []
    n = len(values)
    for i in range(n):
        m = len(operands[i])
        if part == 1:
            combinations = list(product(['+','*'], repeat = m-1))
        elif part == 2:
            combinations = list(product(['+','*','||'], repeat = m-1))
        for tup in combinations:
            result = computeEquation(operands[i],tup)
            if result == values[i]:
                calibrated_result += values[i]
                break
    return calibrated_result

values = []
operands = [] 

with open("../inputs/Input_Day_07.txt","r") as file:
    data = file.readlines() 
    for line in data:
        input = line.strip().split(":")
        values.append(int(input[0]))
        operands.append(list(int(n) for n in input[1].strip().split()))
    print(calculateCalibrationResult(1))        # Problem - Part 1
    print(calculateCalibrationResult(2))        # Problem - Part 2



# Sample Input:
# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20

# Sample Output:
# 3749
# 11387