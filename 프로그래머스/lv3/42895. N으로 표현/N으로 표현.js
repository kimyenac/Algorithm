function solution(N, number) {
    let s = Array.from(new Array(9), () => new Set());
    s.forEach((element, index) => {
        if (index !== 0) element.add(Number(String(N).repeat(index)));
    })
    
    for (let i = 1; i <= 8; ++i) {
        for (let j = 1; j < i; ++j) {
            for (const op1 of s[j]) {
                for (const op2 of s[i-j]) {
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if (op2 !== 0) { 
                        s[i].add(op1 / op2)
                    }
                }
            }
        }
        if (s[i].has(number)) {
            return i;
        }
    }
    return -1
}