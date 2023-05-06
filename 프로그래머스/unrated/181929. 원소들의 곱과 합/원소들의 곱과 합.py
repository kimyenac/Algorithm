def solution(num_list):
    answer = num_list[0]
    for num in num_list[1:]:
        answer *= num
    return 1 if answer < sum(num_list) ** 2 else 0