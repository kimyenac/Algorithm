function solution(orders, course) {
    var answer = [];
    let menu = new Map();

    function combination(order, idx, len, prev) {
        if (prev.length === len) {
            let cur_key = prev.sort().join('');
            if (menu.has(cur_key)) {
                menu.set(cur_key, menu.get(cur_key) + 1);
            } else menu.set(cur_key, 1);
            return;
        }
        
        for (let i = idx; i < order.length; i++) {
            combination(order, i + 1, len, [...prev, order[i]]);
        }
    }

    orders.map(order => {
        course.map(num => combination(order, 0, num, []));
    })

    menu = [...menu.entries()].filter(item => item[1] > 1).sort((a, b) => b[1] - a[1]).sort((a, b) => a[0].length - b[0].length);

    for (const num of course) {
        let max = 0
        let i = 0;
        for (const [x, y] of menu) {
            if (x.length != num) {
                menu.splice(0, i)
                break;
            }
            if (max == 0) {
                max = y;
            }
            if (y == max) {
                answer.push(x)
            }
            i += 1;
        }
    }

    return answer.sort();
}