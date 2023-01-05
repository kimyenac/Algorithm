def solution(numbers):
    answer = ''
    
    alpha = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    
    for i in range(len(numbers)):
        for key in alpha.keys():
            if (numbers[i] == key[0] and numbers[i:len(key)+i] == key):
                answer += str(alpha[key])
    
    return int(answer)