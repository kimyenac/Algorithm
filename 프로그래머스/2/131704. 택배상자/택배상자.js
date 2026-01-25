function solution(order) {
    var answer = 0;
    
    const stack = [];
    const container = [...order].sort();
    
    let box = 1;
    
    for (let i = 0; i < order.length; i++) {
        const target = order[i];
        
        while (box <= order.length && box <= target) {
            stack.push(box);
            box++;
        }
        
        if (target === stack[stack.length - 1]) {
            answer += 1;
            stack.pop()
        } else {
            break;
        }
    }
    
    return answer;
}