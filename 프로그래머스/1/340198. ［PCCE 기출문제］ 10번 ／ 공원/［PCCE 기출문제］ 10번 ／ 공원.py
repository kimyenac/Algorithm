def solution(mats, park):
    answer = -1
    # 크기가 큰 매트부터 시도
    mats.sort(reverse=True)

    h = len(park)
    w = len(park[0])

    for row in range(h):
        for col in range(w):
            if park[row][col] != "-1":
                continue

            for mat in mats:
                if answer >= mat:
                    continue

                # 돗자리가 공원을 벗어나지 않는지 먼저 확인
                if row + mat > h or col + mat > w:
                    continue

                can_place = True
                for i in range(mat):
                    # 사람이 있는 지 확인
                    if park[row + i][col:col + mat] != ["-1"] * mat:
                        can_place = False
                        break

                # 현재 위치에서 가능한 가장 큰 돗자리 찾았으니 다음 위치로
                if can_place:
                    answer = mat
                    break 

    return answer