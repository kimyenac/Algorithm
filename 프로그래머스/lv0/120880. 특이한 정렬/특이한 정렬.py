def solution(numlist, n):
    answer = []
    ans = []
    numlist.sort(reverse=True)
    for num in numlist:
        ans.append(abs(num - n))
    rank = sorted(ans)
    for num in rank:
        idx = ans.index(num)
        answer.append(numlist[idx])
        ans.pop(idx)
        numlist.pop(idx)
        
    return answer