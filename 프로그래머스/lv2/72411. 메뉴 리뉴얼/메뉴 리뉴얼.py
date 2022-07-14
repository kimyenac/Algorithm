from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []

    for i in course:
        ans = []
        for j in orders:
            for x in combinations(j, i):
                x = list(x)
                x.sort(key=lambda x:x[0])
                ans.append("".join(x))
        max = Counter(ans).most_common()
        answer += [x for x, y in max if y > 1 and y == max[0][1]]

    return sorted(answer)