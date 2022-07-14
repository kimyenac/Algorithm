def solution(s):
    stack = []

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return stack==[]