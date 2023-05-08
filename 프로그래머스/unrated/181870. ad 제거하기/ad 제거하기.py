def solution(strArr):
    idx = 0
    
    while idx < len(strArr):
        val = strArr[idx]
        isTrue = True
        for j in range(len(val)-1):
            if val[j:j+2] == "ad":
                strArr.pop(idx)
                isTrue = False
                break
        if isTrue:
            idx += 1
    
    return strArr