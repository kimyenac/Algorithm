class MinHeap {
    constructor() {
        this.heap = [ null ];
    }
    
    size() {
        return this.heap.length - 1;
    }
    
    swap(a, b) {
        [ this.heap[a], this.heap[b] ] = [ this.heap[b], this.heap[a] ];
    }
    
    heappush(value) {
        this.heap.push(value);
        let curIdx = this.heap.length - 1;
        let parIdx = (curIdx / 2) >> 0;
        
        while(curIdx > 1 && this.heap[parIdx][1] > this.heap[curIdx][1]) {
            this.swap(parIdx, curIdx)
            curIdx = parIdx;
            parIdx = (curIdx / 2) >> 0;
        }
    }
    
    heappop() {
        const min = this.heap[1];	
        if(this.heap.length <= 2) this.heap = [ null ];
        else this.heap[1] = this.heap.pop();   
        
        let curIdx = 1;
        let leftIdx = curIdx * 2;
        let rightIdx = curIdx * 2 + 1; 
        
        if(!this.heap[leftIdx]) return min;
        if(!this.heap[rightIdx]) {
            if(this.heap[leftIdx][1] < this.heap[curIdx][1]) {
                this.swap(leftIdx, curIdx);
            }
            return min;
        }

        while(this.heap[leftIdx][1] < this.heap[curIdx][1] || this.heap[rightIdx][1] < this.heap[curIdx][1]) {
            const minIdx = this.heap[leftIdx][1] > this.heap[rightIdx][1] ? rightIdx : leftIdx;
            this.swap(minIdx, curIdx);
            curIdx = minIdx;
            leftIdx = curIdx * 2;
            rightIdx = curIdx * 2 + 1;
            
            if(leftIdx >= this.size()) break;
        }

        return min;
    }
}

function solution(jobs) {
    let answer = 0
    let [now, i, start] = [0, 0, -1]
    const heap = new MinHeap();
    jobs.sort((a, b) => a[0]-b[0])
    
    while (jobs.length > i) {
        for (const j of jobs) {
            if (start < j[0] && j[0] <= now) {
                heap.heappush(j)
            }
        }
        if (heap.size() > 0) {
            const current = heap.heappop()
            start = now
            now += current[1]
            answer += (now - current[0])
            i += 1
        } else {
            now += 1
        }
    }
    
    return answer / jobs.length >> 0
}