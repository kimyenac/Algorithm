def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        ans = arr[s:e+1]
        ans.sort(reverse=True)
        for i in range(len(ans)):
            if i < len(ans) - 1:
                if ans[i] > k and ans[i+1] <= k:
                    answer.append(ans[i])
                    break
            else:
                if ans[i] > k:
                    answer.append(ans[i])
                    break
                else:
                    answer.append(-1)
                    break
    return answer