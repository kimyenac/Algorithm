function solution(money) {
    let n = money.length;
    if (n === 1) return money[0];
    
    // 원형이므로 첫 번째 집 털 땐 마지막 집 포함 X
    let dp1 = Array.from({ length: n }).fill(0);
    dp1[0] = money[0];
    dp1[1] = Math.max(money[0], money[1]);
    for (let i = 2; i < n - 1; i++) {
        dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + money[i]);
    }
    
     // 원형이므로 마지막 집 털 땐 첫 번째 집 포함 X
    let dp2 = Array.from({ length: n }).fill(0);
    dp2[0] = 0;
    dp2[1] = money[1];
    for (let i = 2; i < n; i++) {
        dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + money[i]);
    }
    
    return Math.max(dp1[n - 2], dp2[n - 1]);
}