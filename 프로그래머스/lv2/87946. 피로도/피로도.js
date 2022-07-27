function permutations(arr, n) {
    if (n === 1) return arr.map((v) => [v]);
    let result = [];

    arr.forEach((fixed, idx, arr) => {
      const rest = arr.filter((_, index) => index !== idx);
      const perms = permutations(rest, n - 1);
      const combine = perms.map((v) => [fixed, ...v]);
      result.push(...combine);
    });

    return result;
}

function solution(K, dungeons) {
    let answer = -1;
    let tmp = permutations(dungeons, dungeons.length);
    
    for (let i = 0; i < tmp.length; i++) {
        let k = K;
        let ans = 0;
        for (const item of tmp[i]) {
            if (k >= item[0]) {
                ans += 1;
                k -= item[1];
            } else {
                break;
            }
        }
        if (answer < ans) {
            answer = ans;
        }
    }

    return answer
}