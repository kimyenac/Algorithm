def str_to_int(time):
    hh, mm, ss = time.split(":")
    return int(hh) * 3600 + int(mm) * 60 + int(ss)

def int_to_str(time):
    hh = time // 3600
    time %= 3600
    mm = time // 60
    ss = time % 60
    return str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2)

def solution(play_time, adv_time, logs):
    
    # step 1
    play_time_sec = str_to_int(play_time)
    adv_time_sec = str_to_int(adv_time)
    total_time = [0 for _ in range(play_time_sec + 1)]
    
    # step 2
    for i in range(len(logs)):
        start, end = logs[i].split("-")
        start = str_to_int(start)
        end = str_to_int(end)
        total_time[start] += 1
        total_time[end] -= 1
    
    # step 3
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i-1]
        
    # step 4
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i-1]
        
    # step 5
    most_view = 0
    max_time = 0
    for i in range(adv_time_sec-1, play_time_sec):
        if i >= adv_time_sec:
            if most_view < total_time[i] - total_time[i - adv_time_sec]:
                most_view = total_time[i] - total_time[i - adv_time_sec]
                max_time = i - adv_time_sec + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time_sec + 1
                
    # step 6 
    return int_to_str(max_time)