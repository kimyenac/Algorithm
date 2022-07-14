from collections import defaultdict
def solution(tickets):
    answer = []
    ticket = defaultdict(list)
    
    for i in tickets:
        ticket[i[0]].append(i[1])
        ticket[i[0]].sort(reverse=True)
    
    stack = ["ICN"]
    while len(stack) > 0:
        keys = stack[-1]
        if keys not in ticket or len(ticket[keys]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(ticket[keys][-1])
            ticket[keys].pop()
    
    return answer[::-1]