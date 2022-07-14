def solution(msg):
    answer = []
    findDict = {}

    for idx, val in enumerate(range(ord("A"), ord("Z")+1), start=1):
        findDict[chr(val)] = idx

    start = 0
    end = len(msg)

    while True:
        a = msg[start:end]
        if a in findDict:
            answer.append(findDict[a])
            if end >= len(msg):
                return answer
            else:
                findDict[a+msg[end]] = len(findDict) + 1
                start += len(a)
                end = len(msg)
        else:
            end -= 1