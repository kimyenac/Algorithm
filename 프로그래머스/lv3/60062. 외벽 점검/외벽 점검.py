from itertools import permutations
def solution(n, weak, dist):
    answer = []
    m = len(weak)
    weak_point = weak + [i+n for i in weak]
    
    for idx, start in enumerate(weak):
        for friends in permutations(dist):
            cnt = 1
            pos = start
            for f in friends:
                pos += f
                if pos < weak_point[idx+m-1]:
                    cnt += 1
                    pos = [w for w in weak_point[idx+1:idx+m] if w > pos][0]
                else:
                    answer.append(cnt)
                    break
    
    return min(answer) if answer else -1