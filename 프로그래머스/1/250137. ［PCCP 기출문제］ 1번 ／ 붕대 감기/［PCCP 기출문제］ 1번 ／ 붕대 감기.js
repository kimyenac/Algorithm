function solution(bandage, health, attacks) {
    let h = health;
    const [t, x, y] = bandage;
    
    let total = 0;
    let attIdx = 0;
    for (let i = 0; i <= attacks[attacks.length - 1][0]; i++) {
        if (attIdx >= attacks.length && h <= 0) break;
        if (i !== attacks[attIdx][0]) {
            h += x;
            if (total + 1 >= t) {
                h += y;
                total = 0;
            } else {
                total += 1;  
            }
            if (h > health) h = health;
            continue;
        };
        const [a, b] = attacks[attIdx++];
        h -= b;
        total = 0;
        if (h <= 0) return -1;
    }
    
    return h <= 0 ? -1 : h;
}