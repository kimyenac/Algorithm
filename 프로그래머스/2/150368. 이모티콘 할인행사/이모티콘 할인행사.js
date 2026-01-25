function solution(users, emoticons) {
    let answer = [];
    const ratios = [10, 20, 30, 40];
    let bestPlus = -1;
    let bestSales = -1;
    
    const dfs = (idx, choice) => {
        if (idx === emoticons.length) {
            let plus = 0;
            let sales = 0;
            
            for (const [ratio, limit] of users) {
                let sum = 0;
                
                for (let i = 0; i < emoticons.length; i++) {
                    let r = choice[i];
                    if (r >= ratio) {
                        sum += (emoticons[i] * (100 - r) / 100)
                    }
                }
                
                if (sum >= limit) {
                    plus += 1;
                } else {
                    sales += sum;
                }
            }
           
            // 우선순위 : 플러스 서비스 가입자 -> 이모티콘 판매액 최대한 늘리기
            if (bestPlus < plus || (bestPlus === plus && bestSales < sales)) {
                bestPlus = plus;
                bestSales = sales
            }
            
            return;
            
        };
        
        // 0.1 ~ 0.4 까지 ratio 순회해서 모든 경우의 수 체크하기
        for (const r of ratios) {
            choice[idx] = r;
            dfs(idx + 1, choice);
        }
    };
    
    dfs(0, new Array({ length: emoticons.length }))
    
    return [bestPlus, bestSales];
}