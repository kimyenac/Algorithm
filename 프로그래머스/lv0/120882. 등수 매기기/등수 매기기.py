def solution(score):
    answer = []
    for i in range(len(score)):
        score[i] = sum(score[i])
    rank = sorted(score, reverse=True)
    for i in score:
        answer.append(rank.index(i) + 1)
    return answer