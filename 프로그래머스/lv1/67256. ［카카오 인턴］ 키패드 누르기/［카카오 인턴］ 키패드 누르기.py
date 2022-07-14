def solution(numbers, hand):
    answer = ''

    num = {1 : [0, 0], 2: [0, 1], 3 : [0, 2],
           4 : [1, 0], 5: [1, 1], 6 : [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           "*": [3, 0], 0: [3, 1], "#": [3, 2],
           }

    left = num["*"]
    right = num["#"]

    while numbers:
        x = numbers.pop(0)
        now = num[x]
        if x in [1, 4, 7]:
            answer += "L"
            left = num[x]
        elif x in [3, 6, 9]:
            answer += "R"
            right = num[x]
        else:
            now = num[x]
            ll = abs(left[0] - abs(now[0])) + abs(left[1] - abs(now[1]))
            rr = abs(right[0] - abs(now[0])) + abs(right[1] - abs(now[1]))
            if ll > rr:
                answer += "R"
                right = now
            elif rr > ll:
                answer += "L"
                left = now
            else:
                if hand == "left":
                    answer += "L"
                    left = now
                else:
                    answer += "R"
                    right = now

    return answer