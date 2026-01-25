from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    
    today_y, today_m, today_d = today.split('.')
    today_date = datetime(int(today_y), int(today_m), int(today_d))
    
    for i in range(len(privacies)):
        date, alpha = privacies[i].split()
        y, m, d = date.split('.')
        old = datetime(int(y), int(m), int(d))
        for term in terms:
            t, n = term.split()
            if (t != alpha):
                continue
            new = old + relativedelta(months=int(n), days=-1)
            if (new < today_date):
                answer.append(i + 1)
    
    return answer