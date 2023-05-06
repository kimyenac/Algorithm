def solution(a, b, c):
    answer = [a, b, c]
    if answer.count(a) == 2 or answer.count(b) == 2:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    if answer.count(a) == 3:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    return a + b + c