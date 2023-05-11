def solution(my_string, target):
    for i in range(len(my_string) - len(target) + 1):
        if my_string[i:i+len(target)] == target:
            return 1
    
    return 0