def solution(s):
    ans = s.split()
    answer = 0
    for i in range(len(ans)):
        if (ans[i] == "Z"):
            answer -= int(ans[i-1])
        else:
            answer += int(ans[i])
    return answer