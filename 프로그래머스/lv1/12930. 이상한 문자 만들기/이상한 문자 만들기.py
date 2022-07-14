def solution(s):
    
    answer = []
    for s_split in s.split(" "):
        ans = []
        for i, x in enumerate(s_split):
            if i % 2:
                ans.append(x.lower())
            else:
                ans.append(x.upper())
        answer.append("".join(ans))
    
    return " ".join(answer)