def solution(cipher, code):
    return cipher[code-1:len(cipher):code]