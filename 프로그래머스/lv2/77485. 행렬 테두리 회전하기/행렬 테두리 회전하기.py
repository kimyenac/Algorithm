def solution(rows, columns, queries):
    answer = []
    graph = [[0] * (columns+1) for _ in range(rows+1)]
    
    num = 0
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            num += 1
            graph[i][j] = num
            
    for i in queries:
        ans = []
        x1, y1, x2, y2 = i[0], i[1], i[2], i[3]
        temp = graph[x1][y1]
        ans.append(temp)
        for k in range(x1, x2):
            graph[k][y1] = graph[k+1][y1]
            ans.append(graph[k][y1])
        for k in range(y1, y2):
            graph[x2][k] = graph[x2][k+1]
            ans.append(graph[x2][k])
        for k in range(x2, x1, -1):
            graph[k][y2] = graph[k-1][y2]
            ans.append(graph[k][y2])
        for k in range(y2, y1, -1):
            graph[x1][k] = graph[x1][k-1]
            ans.append(graph[x1][k])
        graph[x1][y1+1] = temp
        ans.sort()
        answer.append(ans[0])
    return answer