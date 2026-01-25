number = int(input())

answer = 0

while(int(number // 2) > 0):
    answer += number % 100
    number //= 100

print(answer)