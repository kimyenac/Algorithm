def solution(clothes):
    answer = 1
    hash = {}
    for cloth, type in clothes:
        hash[type] = hash.get(type, 0) + 1
    for type in hash:
        answer *= (hash[type] + 1)
    return answer - 1