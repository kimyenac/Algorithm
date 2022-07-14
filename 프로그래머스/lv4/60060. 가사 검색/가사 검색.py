import bisect
from collections import defaultdict

def func(a, left, right):
    left_idx = bisect.bisect_left(a, left)
    right_idx = bisect.bisect_right(a, right)
    return right_idx - left_idx

def solution(words, queries):
    answer = []
    dic = defaultdict(list)
    dic_reverse = defaultdict(list)
    for word in words:
        dic[len(word)].append(word)
        dic_reverse[len(word)].append(word[::-1])

    for key in dic.keys():
        dic[key].sort()
        dic_reverse[key].sort()

    for query in queries:
        if query[0] != "?":
            answer.append(func(dic[len(query)], query.replace("?", "a"), query.replace("?", "z")))
        else:
            query = query[::-1]
            answer.append(func(dic_reverse[len(query)], query.replace("?", "a"), query.replace("?", "z")))

    return answer