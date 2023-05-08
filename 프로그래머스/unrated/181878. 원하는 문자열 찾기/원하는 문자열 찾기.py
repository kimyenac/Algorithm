def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    
    for i in range(len(myString)-len(pat)+1):
        print(myString[i])
        if myString[i] == pat[0] and myString[i:len(pat)+i] == pat:
            return 1
    
    return 0