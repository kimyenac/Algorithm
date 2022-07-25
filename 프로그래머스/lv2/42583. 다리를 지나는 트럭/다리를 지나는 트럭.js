function solution(bridge_length, weight, truck_weights) {
    let time = 0
    let bridge = Array.from({length: bridge_length}, () => 0);

    while (bridge.length) {
        time += 1
        bridge.shift()
        if (truck_weights.length) {
            let sum = bridge.reduce(function add(a, b) {
                return a + b
            });
            if (sum + truck_weights[0] > weight) {
                bridge.push(0)
            } else {
                bridge.push(truck_weights.shift())
            }
        }   
    }

    return time
}