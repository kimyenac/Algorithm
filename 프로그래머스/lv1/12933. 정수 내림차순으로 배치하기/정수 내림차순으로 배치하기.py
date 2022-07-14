def solution(n):
    L = list(str(int(n)))
    L.sort(reverse=True)
    return int("".join(L))