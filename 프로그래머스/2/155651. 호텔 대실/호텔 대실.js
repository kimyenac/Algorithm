function solution(book_time) {
    var answer = [];
    const ans = [];
    
    for (const [k, v] of book_time) {
      
        const start = k.split(':');
        const end = v.split(':')
        
        ans.push([Number(start[0] * 60) + Number(start[1]), Number(end[0] * 60) + Number(end[1]) + 10])
    }
    
    ans.sort((a, b) => a[0] - b[0])
    
    for (const [k, v] of ans) {
        let i = 0;
        let checked = false;

        // 교체 가능 체크
        while (answer.length > i) {
            const [start, end] = answer[i];
            
            if (end <= k) {
                answer[i] = [k, v];
                checked = true;
                break;
            }
            
            i++;
        }
        
        // 교체 불가하면 +1
        if (!checked) {
            answer.push([k, v])
        }
    }
        
    return answer.length;
}