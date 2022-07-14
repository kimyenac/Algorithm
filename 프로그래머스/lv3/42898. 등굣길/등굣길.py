def solution(m, n, puddles):
    puddles = [[a, b] for [b, a] in puddles]
    graphs = [[0] * (m+1) for _ in range(n+1)]
    graphs[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                graphs[i][j] = 0
            else:
                graphs[i][j] = (graphs[i-1][j] + graphs[i][j-1]) % 1000000007
                
    return graphs[n][m]