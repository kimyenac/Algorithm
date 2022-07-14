from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    hash = defaultdict(list)

    for i in range(len(records)):
        hash[records[i].split()[1]].append(records[i].split()[0])

    for k, v in hash.items():
        time = 0
        times = []
        for i in range(len(v)):
            if len(times) == 0:
                times = v[i].split(":")
            else:
                t_time1 = int(times[0])
                t_time2 = int(times[1])
                times = v[i].split(":")
                hh = int(times[0]) - t_time1
                mm = int(times[1]) - t_time2
                if hh > 0:
                    time += (hh * 60) + mm
                else:
                    time += mm
                times.clear()
        if len(times) != 0:
            hh = 23 - int(times[0])
            mm = 59 - int(times[1])
            if hh > 0:
                time += (hh * 60) + mm
            else:
                time += mm
        hash[k] = time

    hash = dict(sorted(hash.items()))

    for k, v in hash.items():
        if v > fees[0]:
            n = fees[1] + math.ceil((v - fees[0]) / fees[2]) * fees[3]
            answer.append(n)
        else:
            answer.append(fees[1])

    return answer