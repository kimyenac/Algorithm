from collections import defaultdict
from itertools import combinations
def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            for j in combinations(info_key, i):
                tmp_key = "".join(j)
                info_dict[tmp_key].append(info_val)
                
    for key in info_dict.keys():
        info_dict[key].sort()
        
    for query in queries:
        query = query.split()
        query_score = int(query[-1])
        query = query[:-1]
        for i in range(3):
            query.remove("and")
        while "-" in query:
            query.remove("-")
        tmp_q = "".join(query)
        
        if tmp_q in info_dict:
            score = info_dict[tmp_q]
            if len(score) > 0:
                start, end = 0, len(score)
                while start < end:
                    mid = (start + end) // 2
                    if score[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(score) - start)
        else:
            answer.append(0)
    
    return answer