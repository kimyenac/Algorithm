def solution(cacheSize, cities):
    answer = 0
    stack = []
    
    for city in cities:
        city = city.lower()
        if cacheSize == 0:
            stack.append(city)
            answer += 5
        elif city in stack:
            answer += 1
            idx = stack.index(city)
            stack.pop(idx)
            stack.append(city)
        else:
            answer += 5
            if len(stack) >= cacheSize:
                stack.pop(0)
                stack.append(city)
            else:
                stack.append(city)
    
    return answer