str = input()
answer = ''
for s in str:
    if s.isupper():
        answer += s.lower()
    else:
        answer += s.upper()
print(answer)