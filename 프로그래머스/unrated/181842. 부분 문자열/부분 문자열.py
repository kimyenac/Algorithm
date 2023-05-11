def solution(str1, str2):
    
    for i in range(len(str2) - len(str1) + 1):
        if (str2[i:len(str1)+i] == str1):
            return 1
    
    return 0