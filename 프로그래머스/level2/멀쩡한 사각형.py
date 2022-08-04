def gcd(a, b):
    return a if b == 0 else gcd(b, a%b) 

def solution(w,h):
    return w * h - w - h + gcd(w, h)