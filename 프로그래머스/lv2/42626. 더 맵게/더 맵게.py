import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)
    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x+y*2)
        answer += 1
    return answer