def solution(myString):
    myString = list(myString.lower())
    for i in range(len(myString)):
        if myString[i] == 'a':
            myString[i] = 'A'
    return "".join(myString)