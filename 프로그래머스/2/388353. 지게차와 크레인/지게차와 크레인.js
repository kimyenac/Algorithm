// 테두리에서 시작해서 연결된 0(빈칸)만 outside = true 로 마킹
const markOutside = (data) => {
  const n = data.length;
  const m = data[0].length;
  const outside = Array.from({ length: n }, () => Array(m).fill(false));

  const q = [];
  const push = (x, y) => {
    outside[x][y] = true;
    q.push([x, y]);
  };

  for (let x = 0; x < n; x++) {
    if (data[x][0] === 0 && !outside[x][0]) push(x, 0);
    if (data[x][m - 1] === 0 && !outside[x][m - 1]) push(x, m - 1);
  }
  for (let y = 0; y < m; y++) {
    if (data[0][y] === 0 && !outside[0][y]) push(0, y);
    if (data[n - 1][y] === 0 && !outside[n - 1][y]) push(n - 1, y);
  }

  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];

  while (q.length) {
    const [x, y] = q.shift();
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
      if (outside[nx][ny]) continue;
      if (data[nx][ny] !== 0) continue; // 빈칸(0)만 퍼짐
      outside[nx][ny] = true;
      q.push([nx, ny]);
    }
  }

  return outside;
};

// req 칸 (data[x][y]) 가 외부와 맞닿아 있는 지 체크
const check = (data, x, y, checkList, outside) => {
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];

  for (let i = 0; i < 4; i++) {
    const nextX = x + dx[i];
    const nextY = y + dy[i];

    if (
      nextX < 0 || nextX >= data.length ||
      nextY < 0 || nextY >= data[0].length
    ) {
      checkList.push([x, y]);
      break;
    }

    if (data[nextX][nextY] === 0 && outside[nextX][nextY]) {
      checkList.push([x, y]);
      break;
    }
  }

  return [data, checkList];
};

const allCheck = (data, req, isAll) => {
  let storage = data;
  let checkList = [];

  const outside = markOutside(storage);

  for (let x = 0; x < storage.length; x++) {
    for (let y = 0; y < storage[x].length; y++) {
      if (storage[x][y] === req) {
        if (isAll) {
          storage[x][y] = 0;
        } else {
          [storage, checkList] = check(storage, x, y, checkList, outside);
        }
      }
    }
  }

  return [storage, checkList];
};

function solution(storage, requests) {
  let data = storage.map((row) => row.split(""));

  for (const req of requests) {
    let checkList;

    if (req.length === 1) {
      [data, checkList] = allCheck(data, req, false);

      if (checkList.length) {
        for (const [x, y] of checkList) data[x][y] = 0;
      }
    } else {
      [data] = allCheck(data, req[0], true);
    }
  }

  return data.flat().filter((v) => v !== 0).length;
}