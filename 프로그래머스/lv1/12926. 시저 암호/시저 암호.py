def solution(s, n):
    answer = list(s)
    for i in range(len(answer)):
        if answer[i].isupper():
            print(ord(answer[i]) - ord("A"))
            answer[i] = chr((ord(answer[i]) - ord('A') + n)%26 + ord('A'))
        elif answer[i].islower():
            answer[i] = chr((ord(answer[i]) - ord('a') + n)%26 + ord('a'))
    return "".join(answer)