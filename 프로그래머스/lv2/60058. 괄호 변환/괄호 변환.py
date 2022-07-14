def solution(p):
    if len(p) == 0: return p
    answer = rec(p)
    return answer

def spl(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            break
    return u, v

def isCorrect(p):
    stack = []
    for i in p:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == "(":
                    stack.pop()
    return True if len(stack) == 0 else False

def rec(p):
    answer = ""
    if len(p) == 0: return p
    u, v = spl(p)
    if isCorrect(u):
        answer = u + rec(v)
    else:
        tmp = "("
        tmp += rec(v)
        tmp += ")"
        u = u[1:-1]
        for i in u:
            if i == "(":
                tmp += ")"
            else:
                tmp += "("
        answer += tmp
    return answer