import heapq
def solution(n, works):
    answer = 0
    heap = []
    
    for work in works:
        heapq.heappush(heap, (-work, work))

    while n > 0:
        maxi = heapq.heappop(heap)[1]
        if maxi == 0:
            break
        maxi -= 1
        n -= 1
        heapq.heappush(heap, (-maxi, maxi))

    for i, j in heap:
        answer += (j ** 2)

    return answer