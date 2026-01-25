function solution(sequence, k) {
    var answer = [0, sequence.length - 1];
    
    let sum = 0;
    let left = 0;
    
    for (let right = 0; right < sequence.length; right++) {
        sum += sequence[right];
        
        while (sum > k) {
            sum -= sequence[left];
            left += 1;
        }
        
        if (sum === k) {
            if (answer[1] - answer[0] > right - left) {
                answer = [left, right]
            }
        }
        
    }
    
    return answer
}