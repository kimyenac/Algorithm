def solution(arr):
    answer = [0, 0]
    size = len(arr)
    
    def compression(x, y, size):
        start=arr[x][y]
        for i in range(x, x+size):
            for j in range(y, y+size):
                if arr[i][j] != start:
                    size //= 2
                    compression(x, y, size)
                    compression(x, y+size, size)
                    compression(x+size, y, size)
                    compression(x+size, y+size, size)
                    return
        answer[start] += 1
        
    compression(0, 0, size)
    
    return answer