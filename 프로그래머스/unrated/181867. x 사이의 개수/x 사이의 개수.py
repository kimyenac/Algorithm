def solution(myString):
    answer = []
    idx = -1
    for i in range(len(myString)):
        if myString[i] == 'x':
            answer.append(len(myString[idx+1:i]))
            idx = i
    answer.append(len(myString[idx+1:]))
    return answer