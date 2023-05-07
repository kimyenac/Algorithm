def solution(number):
    answer = 0
    for num in number:
        answer += int(num)
    return answer % 9