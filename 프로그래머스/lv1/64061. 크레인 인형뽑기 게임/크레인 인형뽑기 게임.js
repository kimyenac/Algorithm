function solution(board, moves) {
    var answer = 0;

    let temp = [];
    for(let i = 0; i < board[0].length; i += 1){
        let tempArr = [];
        board.map(el => {
            if (el[i] > 0) {
                tempArr.push(el[i]);
            }
        });
        temp.push(tempArr);
    }

    let stack = [];
    for (const idx of moves) {
        if (temp[idx-1].length <= 0) {
            continue;
        }
        const x = temp[idx-1].shift()
        if (stack.length > 0 && stack[stack.length-1] == x) {
            stack.pop()
            answer += 2
        } else {
            stack.push(x)
        }
    }

    return answer;
}