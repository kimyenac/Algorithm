import sys
sys.setrecursionlimit(10**6)

def check(rooms, number):
    if number not in rooms:
        rooms[number] = number + 1
        return number
    ans = check(rooms, rooms[number])
    rooms[number] = ans+1
    return ans

def solution(k, room_number):
    answer = []

    rooms = {}

    for i in room_number:
        answer.append(check(rooms, i))

    return answer