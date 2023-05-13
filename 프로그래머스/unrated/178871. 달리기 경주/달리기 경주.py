def solution(players, callings):
    
    player = { players[i]: i for i in range(len(players)) }

    for x in callings:
        pre_idx, now_idx = player[x] - 1, player[x]
        players[pre_idx], players[now_idx] = players[now_idx], players[pre_idx]
        player[x] -= 1
        player[players[pre_idx + 1]] += 1
    
    return players