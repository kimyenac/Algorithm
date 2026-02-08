function solution(board) {
    const splitBoard = board.map((item) => item.split(''));
    const flatBoard = splitBoard.flat();
    
    const oCnt = flatBoard.filter((item) => item === 'O').length;
    const xCnt = flatBoard.filter((item) => item === 'X').length;
    
    // 선공, 후공 순서가 잘못 되었거나, 더 많이 둔 경우 0 반환
    if (!(oCnt === xCnt || oCnt === xCnt + 1)) return 0;
    
    // 승리해서 게임이 종료되었음에도 그 게임을 진행한 경우 체크
    let xSuccess = 0, oSuccess = 0;
    for (let i = 0; i < 3; i++) {
        // 가로줄 체크
        let item = splitBoard[i].join('');
        if (item === 'OOO') oSuccess += 1;
        if (item === 'XXX') xSuccess += 1;
        // 세로줄 체크
        item = [splitBoard[0][i], splitBoard[1][i], splitBoard[2][i]].join('');
        if (item === 'OOO') oSuccess += 1;
        if (item === 'XXX') xSuccess += 1;
    }
    
    // 대각선 체크
    let diag1 = [splitBoard[0][0], splitBoard[1][1], splitBoard[2][2]].join('');
    let diag2 = [splitBoard[0][2], splitBoard[1][1], splitBoard[2][0]].join('');
    if (diag1 === 'OOO') oSuccess += 1;
    if (diag1 === 'XXX') xSuccess += 1;
    if (diag2 === 'OOO') oSuccess += 1;
    if (diag2 === 'XXX') xSuccess += 1;
    
    if (oSuccess > 0 && oCnt !== xCnt + 1) return 0;
    if (xSuccess > 0 && oCnt !== xCnt) return 0;
    
    return 1;
}