def solution(sides):
    sides.sort(reverse=True)
    return 1 if sides[0] < sum(sides[1:]) else 2