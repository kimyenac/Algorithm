function solution(players, m, k) {
    let answer = 0;
    let active = 0;
    const expire = new Array(players.length).fill(0)
    
    for (let i = 0; i < players.length; i++) {
        active -= expire[i];
        const need = Math.floor(players[i] / m);
        
        if (need > active) {
            const add = need - active;
            active += add;
            answer += add;
            expire[i + k] = add;
        }
    }
    
    return answer;
}