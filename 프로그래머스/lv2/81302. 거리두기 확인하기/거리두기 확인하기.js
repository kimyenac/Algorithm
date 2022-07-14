const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];
function bfs(x, y, place, chkb, n, m) {
    chkb[x][y] = true;
    const q = [];
    q.push([x, y])
    while (q.length) {
        const [ex, ey] = q.splice(0, 1)[0];
        for (let k = 0; k < 4; k += 1) {
            let nx = ex + dx[k];
            let ny = ey + dy[k];
            if (0<=nx && nx<n && 0<=ny && ny<m && chkb[nx][ny] == false) {
                if (place[nx][ny] == "P") {
                    return false
                }
                if (place[nx][ny] == "O" && place[ex][ey] != "O") {
                    chkb[nx][ny] = true;
                    q.push([nx, ny])
                }
            }
        }
    }

    return true
}

function solution(places) {
    var answer = [];

    var n = places.length;
    var m = places[0].length;

    for (const place of places) {
        const chkb = Array.from(Array(n), () => Array(m).fill(false));
        let discrim = true;
        for (let i = 0; i < n; i += 1) {
            for (let j = 0; j < m; j += 1) {
                if (place[i][j] == "P" && chkb[i][j] == false) {
                    if (bfs(i, j, place, chkb, n, m) == false) {
                        discrim = false;
                        break;
                    }
                }
            }
        }
        if (discrim == true) {
            answer.push(1)
        } else {
            answer.push(0)
        }
    }

    return answer;
}

console.log(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))