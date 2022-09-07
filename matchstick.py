"""
def even_divide(lst, num_piece=4):
    return [
        [lst[i] for i in range(len(lst)) if (i % num_piece) == r]
        for r in range(num_piece)
    ]
"""

def howSum(number, my_list):
    if number in my_list:
        return True
    for a in my_list:
        if number-a in my_list:
            return True
        else:
            my_list.remove(a)
            return howSum(number-a, my_list)
    return False

def makesquare(matchsticks):
    allsum = sum(matchsticks)
    maxnum = max(matchsticks)
    
    if (allsum % 4 != 0):
        return False
    if allsum/4 < maxnum:
        return False
    if howSum(allsum/4, matchsticks):
        return True
    
