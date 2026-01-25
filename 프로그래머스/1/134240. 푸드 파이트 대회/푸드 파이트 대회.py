def solution(food):
    answer = []
    
    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            answer.append(str(i))
    
    return "".join(answer) + str(0) + "".join(answer[::-1])