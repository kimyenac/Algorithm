def solution(n, times):
    answer = max(times) * n
    
    left = min(times)
    right = max(times) * n
    
    while left <= right:
        total = 0
        mid = (left + right) // 2
        for i in range(len(times)):
            total += mid // times[i]
        if total >= n:
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1
    
    return answer