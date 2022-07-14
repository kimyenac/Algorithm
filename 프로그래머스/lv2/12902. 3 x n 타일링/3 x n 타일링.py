def solution(n):
    res = [0, 3, 11]
    idx = int(n/2)
    
    if n % 2 != 0: return 0

    for i in range(3, idx+1):
        res.append((3*res[i-1]+sum(res[1:i-1])*2+2)%1000000007)
        
    return res[idx]