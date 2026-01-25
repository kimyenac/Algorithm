function solution(n, w, num) {
    // 꼭대기 층
    if (n - num <= w) return 1;
    
    const totalRow = Math.ceil(n / w);
    const row = Math.ceil(num / w);
   
    let r1 = n % w;
    let r2 = num % w;
    let answer = totalRow - row;
    
    if (totalRow % 2 === row % 2) {
        if (r1 >= r2) {
            answer++;
        }
    } else {
        if (!r1) r1 = w;
        if (!r2) r2 = w;
        if (r1 + r2 >= w) answer++;
    }
    
    return answer;
}