def solution(s):
    answer = []
    
    for i in range(len(s)):
        if (s[i] in s[:i]):
            x = 0
            for j in range(i):
                if (s[j] == s[i]):
                    x = i - j
            answer.append(x)
        else:
            answer.append(-1)
    
    return answer