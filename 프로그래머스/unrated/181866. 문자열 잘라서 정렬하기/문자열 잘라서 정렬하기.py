def solution(myString):
    answer = myString.split('x')
    return [x for x in sorted(answer) if len(x) > 0]