def solution(before, after):
    after = list(after)
    for i in before:
        if i not in after:
            return 0
        after.pop(after.index(i))
    return 1