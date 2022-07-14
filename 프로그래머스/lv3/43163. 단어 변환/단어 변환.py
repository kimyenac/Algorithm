from collections import deque
def solution(begin, target, words):
    answer = 0
    chkb = [False] * len(words)
    
    def bfs(begin, cnt):
        q = deque()
        nonlocal answer
        q.append((begin, cnt))
        while q:
            word, cnt = q.popleft()
            if word == target:
                answer = cnt
                break
            for i in range(len(words)):
                if not chkb[i]:
                    tmp = 0
                    for j in range(len(word)):
                        if word[j] != words[i][j]:
                            tmp += 1
                    if tmp == 1:
                        q.append((words[i], cnt+1))
                        chkb[i] = True
    
    bfs(begin, 0)
    
    return answer