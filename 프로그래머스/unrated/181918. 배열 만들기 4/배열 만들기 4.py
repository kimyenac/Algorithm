def solution(arr):
    stk = []
    for i in range(len(arr)):
        while len(stk) > 0:
                if stk[-1] < arr[i]:
                    stk.append(arr[i])
                    break
                else:
                    stk.pop()
        if len(stk) == 0:
            stk.append(arr[i])
    return stk