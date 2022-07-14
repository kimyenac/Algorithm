def solution(absolutes, signs):
    answer = 0
    for a, sign in zip(absolutes, signs):
        if sign:
            answer += a
        else:
            answer -= a
    return answer