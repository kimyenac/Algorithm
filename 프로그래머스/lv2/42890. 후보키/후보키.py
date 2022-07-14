from itertools import combinations
def solution(relation):
    
    m = len(relation)
    n = len(relation[0])

    combi = []
    for i in range(1, n+1):
        for j in combinations(range(n), i):
            combi.append(j)
            
    unique = []
    for i in combi:
        ans = [tuple([item[j] for j in i]) for item in relation]
        if len(set(ans)) == m:
            unique.append(i)
            
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    
    return len(answer)