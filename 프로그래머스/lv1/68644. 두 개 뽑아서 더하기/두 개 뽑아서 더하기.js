function combinations(arr, n) {
    if (n === 1) return arr.map((v) => [v]);
    const result = [];
  
    arr.forEach((fixed, idx, arr) => {
      const rest = arr.slice(idx + 1);
      const combis = combinations(rest, n - 1);
      const combine = combis.map((v) => [fixed, ...v]);
      result.push(...combine);
    });
  
    return result;
  }

function solution(numbers) {
    return [...new Set(combinations(numbers, 2).map(combi => combi[0] + combi[1]))].sort((a, b) => a - b)
}