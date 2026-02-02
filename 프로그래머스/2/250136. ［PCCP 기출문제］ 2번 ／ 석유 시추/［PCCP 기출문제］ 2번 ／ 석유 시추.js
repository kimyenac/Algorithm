function solution(land) {
    let answer = 0;
    const n = land.length;
    const m = land[0].length;
    
    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];
    let visited = Array.from({ length: n },
        () => Array.from({ length: m }, () => false));
    let colSum = Array.from({ length: m }).fill(0);
    
    const bfs = (i, j) => {
        let ans = 1;
        let idx = 0;
        const queue = [[i, j]];
        visited[i][j] = true;
        let colTouched = new Set();
        
        while (queue.length > idx) {
            let [x, y] = queue[idx++];
            colTouched.add(y);
            for (let i = 0; i < 4; i++) {
                const nx = dx[i] + x;
                const ny = dy[i] + y;
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && visited[nx][ny] === false && land[nx][ny] === 1) {
                    ans += 1;
                    visited[nx][ny] = true;
                    queue.push([nx, ny]);
                }
            }
        }
        
        for (const c of colTouched) colSum[c] += ans;
    };
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (land[i][j] === 1 && visited[i][j] === false) bfs(i, j);
        }
    }
    
    return Math.max(...colSum);
}