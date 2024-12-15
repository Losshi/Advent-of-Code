# Problem - Part 1
def isCorrectUpdate(order,update):
    for i in range(len(update)-1):
        c_page = update[i]
        for j in range(i+1,len(update)):
            n_page = update[j]
            if [c_page,n_page] not in order:
                return False
    return True

# Problem - Part 2
def getCorrectUpdate(order, update):
    page_position = {page: idx for idx, page in enumerate(update)}
    sorted_update = update[:]
    changed = True
    while changed:
        changed = False
        for c_page, n_page in order:
            if c_page in page_position and n_page in page_position:
                if page_position[c_page] > page_position[n_page]:
                    sorted_update[page_position[c_page]], sorted_update[page_position[n_page]] = sorted_update[page_position[n_page]], sorted_update[page_position[c_page]]
                    page_position[c_page], page_position[n_page] = page_position[n_page], page_position[c_page]
                    changed = True
    return sorted_update


with open("../inputs/Input_Day_05.txt","r") as file:
    data = file.readlines()
    order = []
    updates = []
    for s in data:
        if s.find('|') != -1:
            order.append([int(i) for i in s.split('|')])
        elif s.find(',') != -1:
            updates.append([int(i) for i in s.split(',')])
    
    midSum = 0
    incrctMidSum = 0
    for u in updates:
        if isCorrectUpdate(order,u):
            # Problem - Part 1
            midSum += u[len(u)//2]
        else:
            # Problem - Part 2
            c_update = getCorrectUpdate(order,u)
            incrctMidSum += c_update[len(c_update)//2]
    print(midSum)
    print(incrctMidSum)


# Sample Input:
# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13
#
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47


# Sample Output:
# 143
# 123