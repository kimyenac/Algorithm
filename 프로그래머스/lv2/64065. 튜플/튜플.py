def solution(s):
    answer = []
    ans = []
    
    s = s[1:-1]
    
    while s:
        tmp = []
        x = s[0]
        i = 1
        s = s[i:]
        if x == "{":
            while s[i] != "}":
                i += 1
        x = list(s[:i+1])
        temp = ""
        for j in range(len(x)):
            if x[j].isdigit():
                temp += x[j]
            else:
                tmp.append(int(temp))
                temp = ""
        ans.append(tmp)
        s = s[i+2:]
    
    ans.sort(key=lambda x:len(x))
    
    for i in ans:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer