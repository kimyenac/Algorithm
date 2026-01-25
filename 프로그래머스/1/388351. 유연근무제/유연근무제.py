def check(time):
    h = time // 100
    m = time % 100
    return h * 60 + m

def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        schedule = check(schedules[i]) + 10
        s = startday
        
        trueCheck = True
        for time in timelogs[i]:
            if (s < 6 and check(time) > schedule):
                trueCheck = False
                break;
            s += 1
            if (s == 8):
                s = 1
        
        if (trueCheck):
            answer += 1
    
    return answer