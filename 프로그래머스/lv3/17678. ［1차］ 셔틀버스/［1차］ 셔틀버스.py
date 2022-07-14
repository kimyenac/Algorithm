def solution(n, t, m, timetable):
    ans = 9 * 60 + (n-1) * t
    bus_time = 9 * 60
    timetable = [int(i[:2]) * 60 + int(i[3:]) for i in timetable]
    
    timetable.sort()

    for i in range(n):
        for j in range(m):
            if timetable and timetable[0] <= bus_time:
                answer = timetable.pop(0) - 1
            else:
                answer = ans
        bus_time += t

    answer = str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)

    return answer