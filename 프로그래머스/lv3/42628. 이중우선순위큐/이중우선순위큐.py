import heapq
def solution(operations):
    answer = []
    heap = []

    for i in operations:
        x = i.split()[0]
        y = int(i.split()[1])
        if x == "I":
            heapq.heappush(heap, y)
        else:
            if heap:
                if i == "D 1":
                    heap = heapq.nlargest(len(heap), heap)[1:]
                    heapq.heapify(heap)
                elif i == "D -1":
                    heapq.heappop(heap)

    if heap:
        answer.append(heapq.nlargest(len(heap), heap)[0])
        answer.append(heapq.heappop(heap))
    else:
        answer = [0, 0]

    return answer