import re
from collections import defaultdict
def solution(word, pages):
    word = word.lower()
    urlToIdx = {}
    urlToScore = defaultdict(list)
    urllinkToUrl = defaultdict(list)

    for i in range(len(pages)):
        # 자기 자신 링크 찾기
        page = pages[i].lower()
        url = re.search(r'<meta[^>]*content="https://([\S]*)"/>',page).group(1)
        urlToIdx[url] = i
        # 기본 점수
        basic_score = 0
        for find in re.findall(r'[a-zA-Z]+', page):
            if find == word:
                basic_score += 1
        # 외부 링크 수
        s = set()
        for e in re.findall(r'<a href="https://[\S]*">', page):
            s.add(re.search(r'"https://([\S]*)"', e).group(1))
        urlToScore[url].append(basic_score)
        urlToScore[url].append(len(s))

        # key를 참조하는 외부 링크 value
        for e in s:
            urllinkToUrl[e].append(url)

    answer = []
    for k, v in urlToScore.items():
        score = v[0]
        if k in urllinkToUrl:
            for u in urllinkToUrl[k]:
                score += urlToScore[u][0] / urlToScore[u][1]
        answer.append([score, urlToIdx[k]])

    return sorted(answer, key=lambda x:[-x[0], x[1]])[0][1]