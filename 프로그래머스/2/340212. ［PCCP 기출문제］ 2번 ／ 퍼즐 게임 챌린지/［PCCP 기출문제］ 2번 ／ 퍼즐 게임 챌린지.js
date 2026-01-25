function solution(diffs, times, limit) {
    var answer = Infinity;
    let start = 1;
    let end = 300001;
    
    while (start <= end) {
        const curr = Math.floor((start + end) / 2);
        let lm = limit;
        let i = 0;
        while (lm >= 0 && i < diffs.length) {
            let diff = diffs[i], time = times[i];
            const prevTime = i === 0 ? 0 : times[i-1]
            if (diff > curr) {
                lm -= (diff - curr) * (time + prevTime) + time
            } else {
                lm -= time
            }
            i += 1;
        }
        if (lm >= 0) {
            answer = Math.min(answer, curr);
            end = curr - 1;
        } else {
            start = curr + 1;
        }
    }
    
    return answer;
}