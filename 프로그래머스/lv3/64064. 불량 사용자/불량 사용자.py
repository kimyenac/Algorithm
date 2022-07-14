from itertools import permutations
def check(x, y):
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        if y[i] == "*":
            continue
        if x[i] != y[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer = []
    
    for x in permutations(user_id, len(banned_id)):
        cnt = 0
        for i, j in zip(x, banned_id):
            if check(i, j):
                cnt += 1
        if cnt == len(banned_id):
            if set(x) not in answer:
                answer.append(set(x))
    
    return len(answer)