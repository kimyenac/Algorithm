def solution(wallpaper):
    answer = []
    
    lux, luy = -1, -1
    rdx, rdy = -1, -1
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if lux == -1 and luy == -1:
                    lux = i
                    luy = j
                elif luy > j:
                    luy = j
                else:
                    if (rdx < i + 1):
                        rdx = i + 1
                    if (rdy < j + 1):
                        rdy = j + 1
                        
    if rdx == -1 and rdy == -1:
        rdx, rdy = lux + 1, luy + 1
    
    return [lux, luy, rdx, rdy]