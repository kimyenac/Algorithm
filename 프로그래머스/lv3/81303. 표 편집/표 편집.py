def solution(n, k, cmd):
    link = {}
    for i in range(1, n+1):
        link[i] = [i-1, i+1]
    OX = ["O" for i in range(1, n+1)]

    trash = []
    k += 1
    for i in cmd:
        md = i.split()
        if md[0] == "D":
            i = 0
            while i < int(md[1]):
                k = link[k][1]
                i += 1
        elif md[0] == "C":
            prev, next = link[k]
            trash.append((prev, next, k))
            OX[k-1] = "X"
            if next == n+1:
                k = prev
            else:
                k = next
            if next == n+1:
                link[prev][1] = next
            elif prev == 0:
                link[next][0] = prev
            else:
                link[prev][1] = next
                link[next][0] = prev
        elif md[0] == "U":
            i = 0
            while i < int(md[1]):
                k = link[k][0]
                i += 1
        else:
            prev, next, now = trash.pop()
            OX[now-1] = "O"
            if next == n + 1:
                link[prev][1] = now
            elif prev == 0:
                link[next][0] = now
            else:
                link[prev][1] = now
                link[next][0] = now

    return "".join(OX)