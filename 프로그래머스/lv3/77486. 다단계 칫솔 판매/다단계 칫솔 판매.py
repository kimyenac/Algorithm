import math
from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = []

    graph = defaultdict(list)
    center = "center"
    # 연결된 사람들을 리스트 형태로 만들기
    for i, j in zip(enroll, referral):
        if j == "-":
            graph[i].append(center)
        else:
            graph[i].append(j)

    # 정답을 담을 딕셔너리
    ans = defaultdict(int)
    for i in range(len(seller)):
        val = amount[i] * 100
        key = seller[i]
        if val * 0.1 >= 1:
            ans[key] += math.trunc(val - (val * 0.1))
            val = math.trunc(val * 0.1)
            k = graph[key][0]
            while True:
                if k == "center":
                    break
                if val * 0.1 >= 1:
                    ans[k] += math.trunc(val - math.trunc(val * 0.1))
                    k = graph[k][0]
                    val = math.trunc(val * 0.1)
                else:
                    ans[k] += math.trunc(val)
                    break
        else:
            ans[k] += math.trunc(val)                    

    # 정답을 입력받은 순서대로 출력하기 위해 answer에 저장
    for key in enroll:
        answer.append(ans[key])

    return answer