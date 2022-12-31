def solution(str1, str2):
    size = len(str1) - len(str2)
    for i in range(size+1):
        if (str1[i] == str2[0]):
            if (str1[i:len(str2)+i] == str2):
                return 1
    return 2