function solution(k, d) {
    let answer = 0;
    
    for (let i = 0; i <= d; i += k) {
        const maxX = Math.floor(Math.sqrt(d * d - i * i));
        answer += Math.floor(maxX / k) + 1;
    }
    
    return answer;
}