from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque([(val, idx) for idx, val in enumerate(priorities)])

    while q:
        items = q.popleft()

        if q and max(q)[0] > items[0]:
            q.append(items)
        else:
            answer += 1
            if items[1] == location:
                break

    return answer