from itertools import permutations
def solution(K, dungeons):
    answer = -1

    tmp = []
    for i in permutations(dungeons, len(dungeons)):
        tmp.append(i)

    for i in range(len(tmp)):
        k = K
        ans = 0
        for j in tmp[i]:
            if k >= j[0]:
                ans += 1
                k -= j[1]
            else:
                break
        if answer < ans:
            answer = ans

    return answer