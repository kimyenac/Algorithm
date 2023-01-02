def solution(rsp):
    answer = ""
    for str in rsp:
        if (str == "2"):
            answer += "0"
        elif (str == "0"):
            answer += "5"
        else:
            answer += "2"
    return answer