def solution(arr):
    idx = 0
    answer = []
    while True:
        answer = arr.copy()
        for i in range(len(arr)):
            val = arr[i]
            if val >= 50 and val % 2 == 0:
                arr[i] //= 2
            elif val < 50 and val % 2 != 0:
                arr[i] *= 2
                arr[i] += 1
        if (arr == answer):
            return idx
        idx += 1