import math
def solution(arr):
    
    def lcm(a, b):
        return (a * b) // math.gcd(a, b)
    
    while len(arr) >= 2:
        arr.insert(0, lcm(arr.pop(0), arr.pop(0)))

    return arr[0]