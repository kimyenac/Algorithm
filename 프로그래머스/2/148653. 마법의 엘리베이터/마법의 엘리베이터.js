function solution(storey) {
    let answer = [0, ...[...String(storey)].map((v) => Number(v))];
    
    for (let i = answer.length - 1; i > 0; i--) {
        if (answer[i] < 5) continue;
        if (answer[i] === 5 && answer[i - 1] < 5) continue;
        answer[i] = 10 - answer[i]
        answer[i - 1] += 1
    }
    
    return answer.reduce((a, b) => a+b, 0);
}