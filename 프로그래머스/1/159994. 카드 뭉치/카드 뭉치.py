def solution(cards1, cards2, goal):
    
    for x in goal:
        if (x in cards1):
            if (cards1[0] != x):
                return "No"
            cards1.pop(0)
        if (x in cards2):
            if (cards2[0] != x):
                return "No"
            cards2.pop(0)
    
    return "Yes"