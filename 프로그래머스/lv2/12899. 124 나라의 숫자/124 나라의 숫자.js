function solution(n) {
    let answer = '';

    while (n > 0) {
        if (n % 3 != 0) {
            answer += String(n % 3)
            n = Math.floor(n / 3)
        } else {
            answer += String(4)
            n = Math.floor(n / 3) - 1
        }
    }

    return answer.split("").reverse().join("");
}