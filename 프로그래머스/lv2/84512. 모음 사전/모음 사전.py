from itertools import product
def solution(word):
    
    dict = []
    for i in range(1,6) :
        dict += list(map(''.join, product("AEIOU", repeat=i)))
    dict.sort()
    
    return dict.index(word) + 1