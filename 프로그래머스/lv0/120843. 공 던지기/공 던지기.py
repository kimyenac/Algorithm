def solution(numbers, k):
    ans = 0
    k -= 1
    while k > 0:
        if ((len(numbers) - 1) == ans):
            ans = 1
        elif ((len(numbers) - 2) == ans):
            ans = 0
        else:
            ans += 2
        k -= 1
    return numbers[ans]