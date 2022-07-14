def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        num = s.count('1')
        answer[1] += len(s) - num
        s = bin(num)[2:]
    return answer