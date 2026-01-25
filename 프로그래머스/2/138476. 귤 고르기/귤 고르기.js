function solution(k, tangerine) {
    var answer = 0;
    
    let dict = {};
    tangerine.forEach((key) => dict[key] = (dict[key] || 0) + 1)
    
    const sorted = Object.values(dict).sort((a, b) => b - a)
    
    while (k > 0) {
        k -= sorted[answer]
        answer += 1
    }
    
    return answer;
}