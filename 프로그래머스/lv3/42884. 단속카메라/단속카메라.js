function solution(routes) {
    let answer = 0;
    let camera = -30001;
    routes.sort((a, b) => a[1] - b[1])
    for (const route of routes) {
        if (route[0] > camera) {
            answer += 1
            camera = route[1]
        }
    }
    return answer;
}