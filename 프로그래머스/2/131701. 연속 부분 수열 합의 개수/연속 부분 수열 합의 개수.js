function solution(elements) {
    var answer = new Set();
    const elementList = [...elements, ...elements]
    
    for (let i = 0; i < elements.length; i++) {
        for (let j = 0; j < elements.length; j++) {
            let sum = 0;
            elementList.slice(j, j+i+1).forEach((item) => sum += item);
            answer.add(sum)
        }
    }
    
    return answer.size;
}