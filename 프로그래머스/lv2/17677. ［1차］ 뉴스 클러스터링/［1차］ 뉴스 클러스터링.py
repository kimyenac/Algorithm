def solution(str1, str2):
    list1, list2 = [], []

    ans = ''
    for i in range(1, len(str1)):
        if str1[i - 1].isalpha() and str1[i].isalpha():
            ans += str1[i - 1:i + 1].upper()
        if len(ans) == 2:
            list1.append(ans)
            ans = ''

    for i in range(1, len(str2)):
        if str2[i-1].isalpha() and str2[i].isalpha():
            ans += str2[i-1:i+1].upper()
        if len(ans) == 2:
            list2.append(ans)
            ans = ''

    if len(list1) == 0 and len(list2) == 0:
        answer = 1
    else:
        intersection = []

        union = list1.copy()
        temp = list1.copy()

        for i in list2:
            if i not in temp:
                union.append(i)
            else:
                temp.remove(i)
                intersection.append(i)

        answer = len(intersection) / len(union)

    return int(answer * 65536)