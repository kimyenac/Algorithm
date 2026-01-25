def solution(k, score):
    answer = []
    rank = []
    for s in score:
        if len(rank) < k:
            rank.append(s)
        else:
            if (rank[0] < s):
                rank.pop(0)
                rank.append(s)
        rank.sort()
        answer.append(rank[0])
    return answer