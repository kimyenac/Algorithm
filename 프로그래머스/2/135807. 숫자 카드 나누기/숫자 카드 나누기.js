function gcd(a, b) {
    while (b !== 0) {
        [a, b] = [b, a % b];
    }
    return a;
}

function solution(arrayA, arrayB) {
    let answer = 0;
    const aGcd = arrayA.reduce((a, c) => gcd(a, c));
    const bGcd = arrayB.reduce((a, c) => gcd(a, c))
    
    if (arrayA.every((item) => item % bGcd !== 0)) {
        answer = Math.max(answer, bGcd)
    }
    
     if (arrayB.every((item) => item % aGcd !== 0)) {
        answer = Math.max(answer, aGcd)
    }
    
    return answer;
}