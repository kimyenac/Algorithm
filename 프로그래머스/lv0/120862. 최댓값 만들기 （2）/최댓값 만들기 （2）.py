def solution(numbers):
    max = -1000000000000000
    for i in range(len(numbers)):
        for num in numbers:
            if numbers.index(num) == i:
                continue
            if max < num * numbers[i]:
                max = num * numbers[i]
    return max