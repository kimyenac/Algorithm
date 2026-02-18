function solution(n, m, x, y, r, c, k) {
    let answer = '';
    let dist = Math.abs(x - r) + Math.abs(y - c);
    if (dist > k || (k - dist) % 2 !== 0) return 'impossible';
    
    let cx = x - 1, cy = y - 1;
    let tx = r - 1, ty = c - 1;
    const dx = [1, 0, 0, -1];
    const dy = [0, -1, 1, 0];
    const dir = ['d', 'l', 'r', 'u'];
    
    for (let step = 0; step < k; step++) {
        let movied = false;
        
        for (let i = 0; i < 4; i++) {
            let nx = dx[i] + cx;
            let ny = dy[i] + cy;
            
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            
            let remain = k - (step + 1);
            dist = Math.abs(nx - tx) + Math.abs(ny - ty);
            
            if (remain >= dist && (remain - dist) % 2 === 0) {
                cx = nx;
                cy = ny;
                answer += dir[i];
                movied = true;
                break;
            }
        }
        
        if (!movied) return 'impossible'
    }
    
    return answer;
}