def solution(str_list):
    
    if 'l' not in str_list and 'r' not in str_list:
        return []
    
    l_idx = str_list.index('l') if 'l' in str_list else len(str_list)
    r_idx = str_list.index('r') if 'r' in str_list else len(str_list)
    
    return str_list[:l_idx] if l_idx < r_idx else str_list[r_idx+1:]