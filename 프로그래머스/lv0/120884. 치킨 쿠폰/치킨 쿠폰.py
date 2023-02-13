def solution(chicken):
    answer = chicken // 10
    service_chicken = chicken // 10
    coupon = chicken % 10 + service_chicken
    
    while coupon >= 10:
        service_chicken = coupon // 10
        coupon = coupon % 10 + service_chicken
        answer += service_chicken
        
    return answer