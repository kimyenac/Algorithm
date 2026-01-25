const bfs = (maps, idxX, idxY, finalX, finalY, answer, visited) => {
    let i = 0;
    
    const mx = maps.length;
    const my = maps[0].length;
    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];
    const queue = [[idxX, idxY]];

    while (i < queue.length) {
        const [x, y] = queue[i++];

        for (let j = 0; j < 4; j++) {
            let nx = x + dx[j];
            let ny = y + dy[j];
            if (nx >= 0 && ny >= 0 && nx < mx && ny < my && maps[nx][ny] !== 'X' && visited[nx][ny] === false) {
                if (nx === finalX && ny === finalY) {
                    answer[nx][ny] = answer[x][y] + 1;
                    return answer;
                };
                answer[nx][ny] = answer[x][y] + 1;
                queue.push([nx, ny]);
                visited[nx][ny] = true
            }
        }
    }
    
    return -1;
}

function solution(maps) {
    // 시작 위치와 마지막 확인
    const idxX = maps.findIndex((item) => item.includes('S'));
    const idxY = maps[idxX].indexOf('S');
    let finalX = maps.findIndex((item) => item.includes('L'));
    let finalY = maps[finalX].indexOf('L');
    
    const mx = maps.length;
    const my = maps[0].length;
        
    let visited = Array.from({ length: mx }, () => Array(my).fill(false));
    let answer = Array.from({ length: mx }, () => Array(my).fill(0));
    visited[idxX][idxY] = true;
    
    answer = bfs(maps, idxX, idxY, finalX, finalY, answer, visited);
    
    if (answer === -1) return -1;
    
    const finalX2 = maps.findIndex((item) => item.includes('E'));
    const finalY2 = maps[finalX2].indexOf('E');
    const newvisited = Array.from({ length: mx }, () => Array(my).fill(false));
    const result = bfs(maps, finalX, finalY, finalX2, finalY2, answer, newvisited);

    return result === -1 ? -1 : result[finalX2][finalY2];
}