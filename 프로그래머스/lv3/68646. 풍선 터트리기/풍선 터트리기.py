def solution(a):
    
    def check(x):
        k = x[0]
        q = []
        for i in x:
            if k > i:
                k = i
            q.append(k)
        return q
    
    answer = set(check(a) + check(list(reversed(a))))
    
    return len(answer)