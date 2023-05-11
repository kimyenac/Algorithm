def solution(myStr):
    answer = []
    ans = []
    
    myStr = myStr.split('a')
    
    for x in myStr:
        string = x.split('b')
        for s in string:
            if (len(s) > 0):
                ans.append(s)

    for x in ans:
        string = x.split('c')
        for s in string:
            if (len(s) > 0):
                answer.append(s)
    
    return answer if len(answer) > 0 else ["EMPTY"]