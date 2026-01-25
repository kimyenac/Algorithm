def solution(keymap, targets):
    answer = []
    keyList = [list(s) for s in keymap]
    
    for target in targets:
        ans = 0
        isTrue = True
        for t in target:
            idx = 100
            for key in keyList:
                if t in key and idx >= key.index(t) + 1:
                    idx = key.index(t) + 1
            if idx == 100:
                isTrue = False
                break
            else:
                ans += idx
        if isTrue:
            answer.append(ans)
        else:
            answer.append(-1)
    
    return answer