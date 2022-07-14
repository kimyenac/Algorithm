def solution(answers):
    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for idx, answer in enumerate(answers):
        if one[idx % len(one)] == answer:
            score[0] += 1
        if two[idx % len(two)] == answer:
            score[1] += 1
        if three[idx % len(three)] == answer:
            score[2] += 1

    ans = []
    for idx, answer in enumerate(score, start=1):
        if max(score) == answer:
            ans.append(idx)
    return ans