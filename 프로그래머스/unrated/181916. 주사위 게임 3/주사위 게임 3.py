def solution(a, b, c, d):
    answer = [a, b, c, d]
    answer.sort()
    
    # 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
    if answer.count(a) == 4:
        return 1111 * a
    
    # 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
    if answer.count(answer[0]) == 3:
        return (10 * answer[0] + answer[-1]) ** 2
    if answer.count(answer[-1]) == 3:
        return (10 * answer[1] + answer[0]) ** 2
    
    # 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
    if answer[0] == answer[1]:
        if answer[2] == answer[3]:
            return (answer[0] + answer[2]) * (abs(answer[0] - answer[2]))
        else:
            return answer[2] * answer[3]
    
    if answer[1] == answer[2]:
        return answer[0] * answer[3]
    
    if answer[2] == answer[3]:
        return answer[0] * answer[1]
    
    return answer[0]