import math

def solution(numer1, denom1, numer2, denom2):
    bunmo = denom1 * denom2
    bunja = (numer1 * denom2) + (numer2 * denom1)
    x = math.gcd(bunmo, bunja)
    return [bunja / x, bunmo / x]
