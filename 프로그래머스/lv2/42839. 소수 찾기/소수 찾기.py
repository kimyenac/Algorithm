from itertools import permutations
import math
def solution(numbers):
    answer = 0
    ans = []
    numbers = list(numbers)
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            j = "".join(j)
            if j not in ["0", "1"] and j[0] != "0":
                ans.append(j)
    ans = list(set(ans))
    for i in ans:
        i = int(i)
        a = True
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                a = False
                break
        if a == True:
            answer += 1
    return answer