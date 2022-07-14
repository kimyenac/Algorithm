def solution(files):
    answer = []
    fList = []

    # 파일명 나누기
    for file in files:
        head, number, tail = '', '', ''
        nchk = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                nchk = True
            elif not nchk:
                head = file[:i+1]
            else:
                tail = file[i+1:]
                break
        fList.append([file, head.upper(), int(number)])

    # Head 부분을 우선으로 사전 정렬 후 같은 Head는 number로 정렬
    fList.sort(key=lambda x:(x[1], x[2]))

    # 정답 최종 정렬
    for i in range(len(fList)):
        answer.append(fList[i][0])

    return answer