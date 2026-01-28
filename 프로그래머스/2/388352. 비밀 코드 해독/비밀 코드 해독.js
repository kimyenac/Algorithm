function solution(n, q, ans) {
    var answer = 0;
    const qSet = q.map(arr => new Set(arr));
    
    for (let a = 1; a <= n - 4; a++) {
        for (let b = a + 1; b <= n - 3; b++) {
            for (let c = b + 1; c <= n - 2; c++) {
                for (let d = c + 1; d <= n - 1; d++) {
                    for (let e = d + 1; e <= n; e++) {
                        let arr = [a, b, c, d, e];
                        
                        let isOk = true;
                        for (let i = 0; i < qSet.length; i++) {
                            let count = 0;
                            for (const num of arr) {
                                if (qSet[i].has(num)) count++
                            }
                            if (ans[i] !== count) {
                                isOk = false;
                                break;
                            }
                        }
                        if (isOk) {
                            answer += 1
                        }
                    }
                }
            }
        }
    }
    
    return answer;
}