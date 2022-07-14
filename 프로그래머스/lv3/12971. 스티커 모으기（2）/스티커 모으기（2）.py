def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = sticker[0]
    dp[0][1] = sticker[0]
    dp[1][1] = sticker[1]
    
    for i in range(2, n-1): # 첫 번째 스티커를 사용한 경우
        dp[0][i] = max(dp[0][i-2]+sticker[i], dp[0][i-1])
    
    for i in range(2, n): # 첫 번째 스티커를 사용하지 않은 경우
        dp[1][i] = max(dp[1][i-2]+sticker[i], dp[1][i-1])
    
    answer = max(max(dp[0]), max(dp[1]))

    return answer