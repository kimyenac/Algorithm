class Deque {
    constructor() {
      this.arr = [];
      this.head = 0;
      this.tail = 0;
    }
    push_front(item) {
      if (this.arr[0]) {
        for (let i = this.arr.length; i > 0; i--) {
          this.arr[i] = this.arr[i - 1];
        }
      }
      this.arr[this.head] = item;
      this.tail++;
    }
    push_back(item) {
      this.arr[this.tail++] = item;
    }
    pop_front() {
      if (this.head >= this.tail) {
        return null;
      } else {
        const result = this.arr[this.head++];
        return result;
      }
    }
    pop_back() {
      if (this.head >= this.tail) {
        return null;
      } else {
        const result = this.arr[--this.tail];
        return result;
      }
    }
    isEmpty() {
        return this.head == this.tail;
    }
  }

function solution(begin, target, words) {

    function bfs(begin, target, words) {
        const q = new Deque();
        const chkb = Array(words.length).fill(false);
        q.push_back([begin, 0])
        while (!q.isEmpty()) {
            const [x, c] = q.pop_front();
            if (x == target) {
                return c
            }
            for (let i = 0; i < words.length; i += 1) {
                if (chkb[i] == true) {
                    continue;
                }
                let cnt = 0;
                for (let j = 0; j < words[0].length; j += 1) {
                    if (words[i][j] != x[j]) {
                        cnt += 1;
                    }
                }
                if (cnt == 1) {
                    chkb[i] = true
                    q.push_back([words[i], c + 1])
                }
            }
        }
        return 0;
    }

    var answer = bfs(begin, target, words);

    return answer;
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))