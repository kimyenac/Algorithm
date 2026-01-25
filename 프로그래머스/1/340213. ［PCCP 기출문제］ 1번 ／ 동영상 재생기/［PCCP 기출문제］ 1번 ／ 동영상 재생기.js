function solution(video_len, pos, op_start, op_end, commands) {
    let answer = '';
    
    let videoLenNum = Number(video_len.split(':')[0]) * 60 + Number(video_len.split(':')[1]);
    let posNum = Number(pos.split(':')[0]) * 60 + Number(pos.split(':')[1]);
    let opStartNum = Number(op_start.split(':')[0]) * 60 + Number(op_start.split(':')[1]);
    let opEndNum = Number(op_end.split(':')[0]) * 60 + Number(op_end.split(':')[1]);
    
    for (const com of commands) {
        if (opStartNum <= posNum && posNum <= opEndNum) {
            posNum = opEndNum;
        }
        if (com === 'next') {
            posNum = posNum + 10 >= videoLenNum ? videoLenNum : posNum + 10;
        }
        if (com === 'prev') {
            posNum = posNum - 10 <= 0 ? 0 : posNum - 10;
        }
    }
    
    if (opStartNum <= posNum && posNum <= opEndNum) {
        posNum = opEndNum;
    }
    
    let h = Math.floor(posNum / 60);
    let m = posNum % 60;
    
    h = h < 10 ? '0' + h : h
    m = m < 10 ? '0' + m : m
    
    return h + ':' + m;
}