function solution(k, ranges) {
    var answer = [];
    
    // 우박수열 만들기
    let arr = [k];
    while (k !== 1) {
        if (k % 2 === 0) k /= 2;
        else k = k * 3 + 1;
        arr.push(k);
    }
    
    var areaArr = [];
    for(var i = 0;i < arr.length-1;i++){
        areaArr.push((arr[i]+arr[i+1])/2);
    }

    //각각의 정적분 구하기
    var areaLen = areaArr.length;
    var lastIdx, firstIdx;
    var pushSum;
    for(var i =0;i<ranges.length;i++){
        pushSum = 0;
        lastIdx = areaLen + ranges[i][1];
        firstIdx = ranges[i][0];
        if(lastIdx< firstIdx){
            pushSum = -1;
        }
        else{
            for(var k = firstIdx;k<lastIdx;k++){
                pushSum += areaArr[k];
            }
        }
      
        answer.push(pushSum);
    }   
    return answer;
}