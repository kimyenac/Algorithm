def solution(my_string):
    answer = ''
    return "".join([str for str in my_string if str not in ['a', 'e', 'i', 'o', 'u']])