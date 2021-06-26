def solution(x):
    src = x
    hs = 0
    while x:
        if x >= 1 and x <= 10000:
            hs += x % 10 
            x = x//10
    
    if src % hs == 0:
        answer = True
    else:
        answer = False
    
    return answer