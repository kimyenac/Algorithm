def solution(n):
    rs = [0, 1, 2]
    
    for i in range(3, n+1):
        rs.append((rs[i-1] + rs[i-2]) % 1000000007)
    
    return rs[-1]