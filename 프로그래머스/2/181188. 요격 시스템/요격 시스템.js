function solution(targets) {
    let answer = 0;
    
    targets.sort((a, b) => a[1] - b[1]);
    let end = 0;
    
    for (const t of targets) {
        if (t[0] >= end) {
            end = t[1];
            answer += 1;
        }
    }
    
    return answer;
}