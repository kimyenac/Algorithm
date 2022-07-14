def solution(s):
    answer = 0

    s = list(s)

    for k in range(len(s)):
        stack = []
        ans = 0
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    ans += 2
                    stack.pop()
            elif s[i] == ']':
                if stack and stack[-1] == '[':
                    ans += 2
                    stack.pop()
            else:
                if stack and stack[-1] == '{':
                    ans += 2
                    stack.pop()
        if ans == len(s) and not stack:
            answer += 1
        x = s.pop(0)
        s.append(x)

    return answer