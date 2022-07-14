function solution(n, times) {
    let answer = n * Math.max.apply(null, times);
    let left = 1;
    let right = n * Math.max.apply(null, times);
    
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        let total = 0;
        for (let i = 0; i < times.length; i += 1) {
            total += Math.floor(mid / times[i])
        }
        if (total >= n) {
            right = mid - 1;
            answer = Math.min(answer, mid)
        } else {
            left = mid + 1
        }
    }
    
    return answer;
}