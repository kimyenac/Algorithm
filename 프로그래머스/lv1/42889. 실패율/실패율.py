from collections import defaultdict
def solution(N, stages):
    ans = defaultdict(float)
    n = len(stages)

    for i in range(1, N+1):
        x = 0
        for j in stages:
            if i == j:
                x += 1
        if x == 0:
            ans[i] = x
        else:
            ans[i] = x/n
        n -= x

    ans = dict(sorted(ans.items(), key=lambda x:(x[1], -x[0]), reverse=True))

    return list(ans.keys())