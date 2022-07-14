function solution(s) {
    var answer = "";

    alpha = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5,
            "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9};

    let str = ""
    for (let i of s) {
        if (!isNaN(i)) {
            answer += i
        } else {
            str += i
            if (str in alpha) {
                answer += String(alpha[str])
                str = ""
            }
        }
    }

    return Number(answer);
}