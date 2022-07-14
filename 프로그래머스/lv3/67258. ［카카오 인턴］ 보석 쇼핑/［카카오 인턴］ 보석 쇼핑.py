def solution(gems):
    check = len(set(gems))
    start = 0
    end = 0
    mins = len(gems)+1
    ans = {}
    while end < len(gems):
        if gems[end] not in ans:
            ans[gems[end]] = 1
        else:
            ans[gems[end]] += 1
        end += 1
        if check == len(ans):
            while start < end:
                if ans[gems[start]] > 1:
                    ans[gems[start]] -= 1
                    start += 1
                elif mins > end - start:
                    mins = end - start
                    answer = [start + 1, end]
                    break
                else:
                    break

    return answer