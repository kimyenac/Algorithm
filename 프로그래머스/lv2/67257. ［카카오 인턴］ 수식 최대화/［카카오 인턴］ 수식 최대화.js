function permutations(arr, n) {
    if (n === 1) return arr.map((v) => [v]);
    let result = [];
  
    arr.forEach((fixed, idx, arr) => {
      const rest = arr.filter((_, index) => index !== idx);
      const perms = permutations(rest, n - 1);
      const combine = perms.map((v) => [fixed, ...v]);
      result.push(...combine);
    });
  
    return result;
  }

function check(ope, arr) {
    for (const o of ope) {
        while (arr.includes(o)) {
            let i = arr.indexOf(o);
            if (o == "+") {
                x = arr[i-1] + arr[i+1]
            }
            if (o == "-") {
                x = arr[i-1] - arr[i+1]
            }
            if (o == "*") {
                x = arr[i-1] * arr[i+1]
            }
            arr.splice(i-1, 0, x);
            arr.splice(i, 1);
            arr.splice(i, 1);
            arr.splice(i, 1);
            }
        }
    return Math.abs(arr[0])
}

function solution(expression) {
    var answer = 0;

    const stack = [];
    let num = ""
    for (let i = 0; i < expression.length; i += 1) {
        if (i == expression.length-1) {
            num += expression[i]
            stack.push(Number(num))
        }
        if (isNaN(expression[i])) {
            if (num) {
                stack.push(Number(num))
                num = ""
            }
            stack.push(expression[i])
        } else {
            num += expression[i]
        }
    }
    let op = ["+", "*", "-"];
    const operator = permutations(op, 3)

    for (const ope of operator) {
        let arr = stack.slice()
        let x = check(ope, arr)
        if (x > answer) {
            answer = x
        }
    }

    return answer;
}