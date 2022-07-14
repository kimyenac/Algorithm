function solution(msg) {
    var answer = [];
    const alpha = new Map();

    for (let i = "A".charCodeAt(0); i <= "Z".charCodeAt(0); i += 1) {
        alpha[String.fromCharCode(i)] = i - ("A".charCodeAt(0) - 1)
    }

    let start = 0;
    let end = start + 1;
    while (msg.length) {
        let x = msg.slice(start, end)
        if (!(x in alpha)) {
            alpha[x] = Object.keys(alpha).length + 1
            answer.push(alpha[msg.slice(start, end-1)])
            msg = msg.slice(end-1, msg.length)
            start = 0;
            end = start + 1;
            continue;
        }
        if (end == msg.length) {
            answer.push(alpha[x])
            break;
        }
        end += 1
    }

    return answer;
}