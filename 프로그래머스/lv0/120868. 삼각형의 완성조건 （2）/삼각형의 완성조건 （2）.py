def solution(sides):
    answer = 0
    max_number = max(sides)
    min_number = min(sides)
    sum_number = sum(sides)
    
    # 가장 긴 변이 sides의 max 값인 경우
    number = 1
    while True:
        new_num = min_number + number;
        if (number > max_number):
            break
        if (new_num > max_number):
            answer += 1
        number += 1
        
    # 가장 긴 변이 나머지 한 변인 경우
    num = max_number + 1
    while True:
        if (num < sum_number):
            answer += 1
        else:
            break
        num += 1
    
    return answer