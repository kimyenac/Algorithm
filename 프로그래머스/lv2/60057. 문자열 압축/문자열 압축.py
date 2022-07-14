def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        res = ''
        tmp = s[0:step]
        cnt = 1
        for i in range(step, len(s), step):
            if tmp == s[i:i+step]:
                cnt += 1
            else:
                res += str(cnt) + tmp if cnt >= 2 else tmp
                tmp = s[i:i+step]
                cnt = 1
        res += str(cnt) + tmp if cnt >= 2 else tmp
        answer = min(answer, len(res))
    return answer