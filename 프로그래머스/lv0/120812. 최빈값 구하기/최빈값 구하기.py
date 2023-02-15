def solution(array):
    dictionary = {}
    
    for arr in array:
        dictionary[arr] = array.count(arr)
        
    max_count = max(dictionary.values())
    
    ans = 0
    for key, val in dictionary.items():
        if val == max_count:
            answer = key
            ans += 1
    
    if (ans > 1):
        return -1
    
    return answer