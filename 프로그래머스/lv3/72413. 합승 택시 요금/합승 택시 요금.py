import heapq
def solution(n, s, a, b, fares):
    def dijkstra(start):
        distance = [float('INF') for _ in range(n+1)]
        distance[start] = 0
        q = []
        heapq.heappush(q, (distance[start], start))
        while q:
            result_x, x = heapq.heappop(q)
            for fu, fw in graph[x]:
                next_val = result_x + fw
                if distance[fu] > next_val:
                    distance[fu] = next_val
                    heapq.heappush(q, (next_val, fu))
        return distance
    
    answer = 9876543210
    graph = [[] for _ in range(n+1)]
    for i, j, c in fares:
        graph[i].append((j, c))
        graph[j].append((i, c))
    
    dp = [[]]
    for i in range(1, n+1):
        dp.append(dijkstra(i))
        
    for i in range(1, n+1):
        answer = min(answer, dp[s][i] + dp[i][a] + dp[i][b])
    return answer