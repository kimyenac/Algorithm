function solution(plans) {
    let answer = [];
    
    // 시작 시간 기준으로 정렬
    let planList = plans.map((p) => [p[0], Number(p[1].split(':')[0]) * 60 + Number(p[1].split(':')[1]), Number(p[2])]).sort((a, b) => a[1] - b[1]);
    
    let stack = [];
    for (let i = 0; i < planList.length; i++) {
        const [name, start, play] = planList[i];
        let nextStart = i < planList.length - 1 ? planList[i+1][1] : Infinity;
        
        // 다음 과제 시작 시간 전까지 가능한 시간
        let free = nextStart - start;
        stack.push([name, play]);
        
        while (stack.length && free > 0) {
            let top = stack[stack.length - 1];
            if (top[1] <= free) {
                free -= top[1];
                answer.push(top[0]);
                stack.pop();
            } else {
                top[1] -= free;
                free = 0;
            }
        }
    }
        
    return answer;
}