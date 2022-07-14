function makeTrie(words) {
    const root = {};
    for (const word of words) {
      let current = root;
      for (const letter of word) {
        if (!current[letter]) current[letter] = [0, {}];
        current[letter][0] = 1 + (current[letter][0] || 0);
        current = current[letter][1];
      }
    }
  
    return root;
  }
function solution(words) {
    var answer = 0;
    const trie = new makeTrie(words);
    
    for (const word of words) {
        let cnt = 0;
        let temp = trie;
        for (const [index, letter] of [...word].entries()) {
            cnt += 1;
            if (temp[letter][0] <= 1) {
                break;
            }
            temp = temp[letter][1]
        }
        answer += cnt
    }
    
    return answer;
}