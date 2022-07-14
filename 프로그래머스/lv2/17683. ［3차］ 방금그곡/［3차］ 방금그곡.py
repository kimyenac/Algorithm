def solution(m, musicinfos):
    answer, music = [], []
    x = -1
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

    for i in musicinfos:
        musics = i.split(',')
        hh1 = int(musics[0].split(':')[0])
        hh2 = int(musics[1].split(':')[0])
        if hh2 - hh1 > 0:
            hh = (hh2 - hh1) * 60
        else:
            hh = 0
        mm1 = int(musics[0].split(':')[1])
        mm2 = int(musics[1].split(':')[1])
        mm = mm2 - mm1
        time = hh + mm
        at = musics[3].replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        if time <= len(at):
            at = at[:time]
        else:
            a, b = divmod(time, len(at))
            at = a * at + at[:b]
        music.append([time, musics[2], at])

    for i in music:
        if m in i[2]:
            x = max(x, i[0])
            answer.append(i)
    
    if len(answer) == 0:
        return "(None)"
    else:
        for i in range(len(answer)):
            if answer[i][0] == x:
                return answer[i][1]