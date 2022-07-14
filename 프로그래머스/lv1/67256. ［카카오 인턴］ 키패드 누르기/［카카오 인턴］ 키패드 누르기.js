function solution(numbers, hand) {
    var answer = '';

    const keypad = {1 : [0, 0], 2 : [0, 1], 3 : [0, 2], 4 : [1, 0], 5 : [1, 1], 6 : [1, 2],
                    7 : [2, 0], 8 : [2, 1], 9 : [2, 2], "*" : [3, 0], 0 : [3, 1], "#" : [3, 2]};

    let left = keypad["*"];
    let right = keypad["#"];

    for (const num of numbers) {
        const now = keypad[num];
        if (num == 1 || num == 4 || num == 7) {
            left = now;
            answer += "L";
            continue;
        }
        if (num == 3 || num == 6 || num == 9) {
            right = now;
            answer += "R";
            continue;
        }
        let l = Math.abs(left[0] - now[0]) + Math.abs(left[1] - now[1]);
        let r = Math.abs(right[0] - now[0]) + Math.abs(right[1] - now[1]);
        if (l > r) {
            right = now;
            answer += "R";
            continue;
        }
        if (r > l) {
            left = now;
            answer += "L";
            continue;
        }
        if (hand == "left") {
            left = now;
            answer += "L";
            continue;
        } else {
            right = now;
            answer += "R";
            continue;
        }
    }

    return answer;
}