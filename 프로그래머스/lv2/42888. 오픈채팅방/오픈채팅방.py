def solution(record):
    answer = []
    rec = []
    userId = {}
    for i in range(len(record)):
        rec.append(record[i].split())
    for i in range(len(rec)):
        user = rec[i][1]
        if len(rec[i]) > 2:
            userId[user] = rec[i][2]
    for i in range(len(rec)):
        if rec[i][0] == "Enter":
            answer.append("{0}님이 들어왔습니다.".format(userId[rec[i][1]]))
        if rec[i][0] == "Leave":
            answer.append("{0}님이 나갔습니다.".format(userId[rec[i][1]]))

    return answer