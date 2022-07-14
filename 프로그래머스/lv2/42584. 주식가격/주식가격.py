def solution(prices):
    answer = []
    for i in range(len(prices)):
        price = 0
        for j in range(i+1, len(prices)):
            price += 1
            if prices[i] > prices[j]:
                break
        answer.append(price)
    return answer