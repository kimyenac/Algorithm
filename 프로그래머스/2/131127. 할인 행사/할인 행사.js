function solution(want, number, discount) {
    var answer = 0;
    let dict = new Map();
    want.forEach((key, idx) => dict.set(key, number[idx]))
    
    for (let i = 0; i < discount.length; i++) {
        const dis = discount.slice(i, i+10);
        let total = new Map();
        
        for (let j = 0; j < dis.length; j++) {
            if (!total.get(dis[j])) {
                total.set(dis[j], 0)
            }
            total.set(dis[j], total.get(dis[j]) + 1)
        }
        
        if ([...dict.keys()].every((key) => dict.get(key) <= total.get(key))) {
            answer += 1;
        }
    }
    
    return answer;
}