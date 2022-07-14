def solution(nums):
    a = list(set(nums))
    if len(a) <= len(nums) / 2:
        return len(a)
    else:
        return len(nums) // 2