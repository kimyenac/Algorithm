import itertools
def solution(spell, dic):
    ans = itertools.permutations(spell, len(spell))
    for i in ans:
        if "".join(list(i)) in dic:
            return 1
    return 2