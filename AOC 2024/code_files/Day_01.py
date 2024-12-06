# Problem - Part 1
def locationDifferenceScore(list_1,list_2):
    list_1.sort() 
    list_2.sort() 
    diff_score = 0
    for i in range(len(list_1)):
        diff_score += abs(list_1[i] - list_2[i])
    return diff_score

# Problem - Part 2
def locationSimilarityScore(list_1,list_2):
    sim_score = 0
    for n in list_1:
        sim_score += (n * list_2.count(n))
    return sim_score

with open("../inputs/Input_Day_01.txt","r") as file:
    data = file.readlines()
    list_1 = []
    list_2 = []
    for line in data:
        record = [int(level) for level in line.split()]
        list_1.append(record[0])
        list_2.append(record[1])
    print(locationDifferenceScore(list_1,list_2)) 
    print(locationSimilarityScore(list_1,list_2))


# Sample Input:
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3

# Sample Output:
# 11
# 31

