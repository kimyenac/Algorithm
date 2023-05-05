# def solution(k, m, score):
#     answer = 0
#     score.sort(reverse=True)
#     while len(score) >= m:
#         answer += score[m-1] * m
#         score = score[m:]
#     return answer

def solution(k, m, score):
    answer = 0
    ans = []
    arr = []
    score.sort(reverse=True)
    ans = [score[i:i+m] for i in range(0, len(score), m)]
    
    for x in ans:
        if (len(x) < m):
            break
        if x in arr:
            continue
        arr.append(x)
        answer += x[-1] * m * ans.count(x)
    
    return answer