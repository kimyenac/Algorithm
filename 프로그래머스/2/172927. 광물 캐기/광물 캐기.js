const getPlus = (idx, mineral) => {
    if (idx === 1) return 1;
    if (idx === 2) {
        if (mineral === 'diamond') return 5;
        return 1;
    }
    if (mineral === 'diamond') return 25;
    if (mineral === 'iron') return 5;
    return 1;
}

function solution(picks, minerals) {
    var answer = 0;
    const maxN = (picks[0] + picks[1] + picks[2]) * 5;
    
    const groups = []
    for (let i = 0; i < minerals.length; i += 5) {
        if (i >= maxN) break;
        const group = minerals.slice(i, i+5);
        groups.push({ group, score: group.map((g) => getPlus(3, g)).reduce((a, c) => a+c) })
    }
    
    groups.sort((a, b) => b.score - a.score);
    
    let j = 0;
    for (let i = 0; i < picks.length; i++) {
        let pick = picks[i] * 5;
        
        while (pick > 0 && j < groups.length) {
            const { group } = groups[j++];
            group.forEach((item) => {
                answer += getPlus(i+1, item)
            })
            pick -= 5;
        }
    }
    
    return answer;
}