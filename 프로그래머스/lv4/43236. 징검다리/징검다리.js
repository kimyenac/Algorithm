function solution(distance, rocks, n) {
    var answer = 0;
    let left = 1;
    rocks.push(distance);
    rocks.sort((a, b) => a - b);
    let right = distance;
    
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        let current = 0;
        let cnt = 0;
        for (const rock of rocks) {
            let diff = rock - current;
            if (diff < mid) {
                cnt += 1
            } else {
                current = rock;
            }
        }
        if (cnt > n) {
            right = mid - 1
        } else {
            left = mid + 1;
            answer = mid
        }
    }
    
    return answer;
}