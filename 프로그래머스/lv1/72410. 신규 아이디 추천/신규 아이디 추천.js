function solution(new_id) {
    let answer = new_id.toLowerCase()
        .replace(/[^a-z0-9-_.]/gi, '')
        .replace(/[.]{2,}/gi, '.')
        .replace(/^[.]|[.]$/gi,'');
    if (answer == "") {
        answer = "a"
    }
    if (answer.length >= 16) {
        answer = answer.substr(0, 15).replace(/[.]$/gi,'')
    }
    if (answer.length <= 2) {
        let x = answer[answer.length-1]
        answer = answer.padEnd(3, x)
    }
    return answer;
}