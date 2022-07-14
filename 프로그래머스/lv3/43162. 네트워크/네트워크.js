function solution(n, computers) {
    var answer = 0;

    const chkb = Array(n).fill(false);
    const graph = Array.from(Array(n), () => new Array());

    for (let i = 0; i < n; i += 1) {
        for (let j = 0; j < n; j += 1) {
            if (computers[i][j] == 1) {
                graph[i].push(j)
            }
        }
    }

    function bfs(x) {
        const q = []
        q.push(x)
        chkb[x] = true;
        while (q.length) {
            let nx = q.shift();
            for (const v of graph[nx]) {
                if (chkb[v] == false) {
                    q.push(v)
                    chkb[v] = true;
                }
            }
        }
    }

    for (let i = 0; i < n; i += 1) {
        if (chkb[i] == false) {
            bfs(i);
            answer += 1;
        }
    }

    return answer;
}