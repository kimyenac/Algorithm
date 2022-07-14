from collections import defaultdict
def solution(genres, plays):
    answer = []

    genre = defaultdict(list)
    for i in range(len(genres)):
        key = genres[i]
        genre[key].append([i, plays[i]])
        val = genre.get(key)
        if len(val) > 1:
            val.pop(0)
            sums = 0
            for i in val:
                sums += i[1]
            val.insert(0, [sums])
        else:
            val.insert(0, [val[0][1]])

    ans = dict(sorted(genre.items(), key=lambda x:x[1][0], reverse=True))

    for key, val in ans.items():
        val = val[1:]
        val.sort(key=lambda x:x[1], reverse=True)
        if len(val) > 2:
            val = val[:2]
        ans[key] = val

    for val in ans.values():
        for i in val:
            answer.append(i[0])

    return answer