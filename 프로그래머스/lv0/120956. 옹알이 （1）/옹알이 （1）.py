from itertools import permutations

def solution(babbling):
    answer = 0
    
    words = []
    array = ["aya", "ye", "woo", "ma"]
    
    for i in range(1, len(array)+1):
        for j in permutations(array, i):
            words.append(''.join(j))
            
    for word in babbling:
        if (word in words):
            answer += 1
        
    return answer