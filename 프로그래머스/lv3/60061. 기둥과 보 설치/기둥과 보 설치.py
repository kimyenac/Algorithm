def pillar_check(pillar_pos, answer):
    x, y = pillar_pos
    if y == 0:
        return True
    if [x, y-1, pillar] in answer or [x-1, y, beam] in answer or [x, y, beam] in answer:
        return True
    return False

def beam_check(beam_pos, answer):
    x, y = beam_pos
    if [x, y-1, pillar] in answer or [x+1, y-1, pillar] in answer:
        return True
    if [x-1, y, beam] in answer and [x+1, y, beam] in answer:
        return True
    return False

def solution(n, build_frame):
    answer = []
    
    global pillar, beam
    pillar, beam = 0, 1
    
    for b in build_frame:
        x, y, kind, oper = b
        if oper == 1:
            if kind == pillar:
                if pillar_check([x, y], answer):
                    answer.append(b[:3])
            else:
                if beam_check([x, y], answer):
                    answer.append(b[:3])
        else:
            temp = answer.copy()
            temp.remove(b[:3])
            check = True
            for t in temp:
                x, y, kind = t
                if kind == pillar:
                    if not pillar_check([x, y], temp):
                        check = False
                        break
                else:
                    if not beam_check([x, y], temp):
                        check = False
                        break
            if check:
                answer = temp.copy()
    
    answer.sort()
    return answer