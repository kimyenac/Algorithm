class MaxHeap {
  constructor() {
    this.h = [];
  }

  push(v) {
    this.h.push(v);
    let i = this.h.length - 1;
    while (i > 0) {
      let p = (i - 1) >> 1;
      if (this.h[p] >= this.h[i]) break;
      [this.h[p], this.h[i]] = [this.h[i], this.h[p]];
      i = p;
    }
  }

  pop() {
    if (this.h.length === 1) return this.h.pop();
    const top = this.h[0];
    this.h[0] = this.h.pop();
    let i = 0;
    while (true) {
      let l = i * 2 + 1;
      let r = i * 2 + 2;
      let m = i;
      if (l < this.h.length && this.h[l] > this.h[m]) m = l;
      if (r < this.h.length && this.h[r] > this.h[m]) m = r;
      if (m === i) break;
      [this.h[i], this.h[m]] = [this.h[m], this.h[i]];
      i = m;
    }
    return top;
  }
}

function solution(n, k, enemy) {
    let answer = 0;
    const heap = new MaxHeap();
   
    for (let i = 0; i < enemy.length; i++) {
        const e = enemy[i];
        heap.push(e);
        n -= e;
        
        if (n < 0) {
            if (k === 0) break;
            n += heap.pop();
            k -= 1;
        }
        answer += 1;
    }
    
    return answer;
}