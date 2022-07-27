function solution(citations) {
    let answer = [];
    citations.sort((a, b) => a - b);
    let n = citations.length;
    for (let h = 0; h <= n; h++) {
        let [ans1, ans2] = [0, 0]
        for (let i = 0; i < n; i++) {
            if (ans2 > h) {
                break;
            } else if (h <= citations[i]) {
                ans1 += 1;
            } else {
                ans2 += 1;
            }
        }
        if (h <= ans1 && h >= ans2) {
            answer.push(h)
        }
    }

    return Math.max(...answer)
}