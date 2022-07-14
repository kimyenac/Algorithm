
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
from itertools import permutations
# 문자열에서 숫자와 연산자 분리하여 stack에 저장 -> 연산자 우선순위 조합 결정하기
# -> 조합한 연산자를 순회하며 각 계산 값을 answer에 저장 -> 가장 큰 값 반환
def solution(expression):
    answer = []
    stack = []
    operator = []

    # 문자열에서 숫자와 연산자 분리하여 stack에 저장
    i = 0
    while expression:
        if i >= len(expression):
            stack.append(int(expression))
            expression = ''
        else:
            x = expression[i]
            if x in ['+', '-', "*"]:
                stack.append(int(expression[:i]))
                stack.append(expression[i])
                expression = expression[i+1:]
                i = -1
            i += 1

    # 연산자 우선순위 조합 결정하기
    for i in permutations(['+', '-', '*'], 3):
        i = list(i)
        operator.append(i)

    # 조합한 연산자를 순회하며 각 계산 값을 answer에 저장
    for i in operator:
        ans = stack.copy()
        for j in i:
            k = 0
            if j in ans:
                while ans:
                    if j not in ans:
                        break
                    if ans[k] == j:
                        if j == '+':
                            x = ans[k-1] + ans[k+1]
                            ans.insert(k-1, x)
                        elif j == '-':
                            x = ans[k - 1] - ans[k + 1]
                            ans.insert(k - 1, x)
                        elif j == '*':
                            x = ans[k - 1] * ans[k + 1]
                            ans.insert(k - 1, x)
                        ans.pop(k)
                        ans.pop(k)
                        ans.pop(k)
                        k = 0
                    k += 1
        answer.append(abs(ans[0]))

    answer.sort(reverse=True)

    return answer[0]