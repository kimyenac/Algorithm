def solution(lottos, win_nums):

    rank=[6, 6, 5, 4, 3, 2, 1]

    cnt_zero = lottos.count(0)
    answer = 0
    for x in win_nums:
        if x in lottos:
            answer += 1
            
    return rank[cnt_zero + answer], rank[answer]