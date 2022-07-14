def solution(s):
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, val in enumerate(num_list):
        s = str(idx).join(s.split(val))
    return int(s)