def solution(s):
    stack = []

    for i in range(len(s)):
        x = s[i]
        if len(stack) == 0 or stack[-1] != x:
            stack.append(x)
        else:
            stack.pop()

    if len(stack) == 0:
        return 1
    else:
        return 0