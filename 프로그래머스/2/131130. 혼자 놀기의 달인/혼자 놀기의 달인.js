function solution(cards) {
    let answer = [];
    let checked = new Set();
    
    const check = (idx) => {
        let id = idx;
        let ans = [];
        while (true) {
            if (checked.has(cards[id - 1])) break;
            ans.push(cards[id - 1]);
            id = cards[id - 1];
            checked.add(id);
        }
        return ans;
    }
    
    for (let i = 0; i < cards.length; i++) {
        const ans = check(i + 1);
        if (ans.length > 0) answer.push(ans.length);
    }
    
    answer.sort((a, b) => b - a);
    
    return answer.length > 1 ? answer[0] * answer[1] : 0;
}