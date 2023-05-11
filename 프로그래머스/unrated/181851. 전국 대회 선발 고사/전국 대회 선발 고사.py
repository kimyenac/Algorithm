def solution(rank, attendance):
    ans = {}
    for i in range(len(rank)):
        if attendance[i]:
            ans[rank[i]] = i
    answer = sorted(ans.items(), key=lambda x:x[0])
    return answer[0][1] * 10000 + answer[1][1] * 100 + answer[2][1]