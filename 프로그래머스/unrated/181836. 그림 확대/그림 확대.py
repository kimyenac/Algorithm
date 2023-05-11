def solution(picture, k):
    answer = []
    for pic in picture:
        ans = ''
        for x in pic:
            ans += x * k
        for _ in range(k):
            answer.append(ans)
    return answer