function solution(weights) {
    var answer = 0;
    const map = new Map();
    
    for (const w of weights) {
        map.set(w, (map.get(w) || 0) + 1)
    }
    
    // 1:1 비율의 짝꿍 체크
    for (const cnt of map.values()) {
        answer += cnt * (cnt - 1) / 2
    }
    
    // 2:4, 2:3, 3:4 비율 체크
    const check = [[2, 4], [2, 3], [3, 4]]
    for (const [k, v] of map.entries()) {
        for (const [a, b] of check) {
            const x = k * a / b;
            if (map.has(x)) {
                answer += v * map.get(x)
            }
        }
    }
    
    return answer;
}