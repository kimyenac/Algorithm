def solution(dots):
    max_x = max([dot[0] for dot in dots])
    min_x = min([dot[0] for dot in dots])
    max_y = max([dot[1] for dot in dots])
    min_y = min([dot[1] for dot in dots])
    
    x = max_x - min_x
    y = max_y - min_y
    
    return x * y