sm = 123257
bg = 647015

total = 0 

def check_cond(num):
    f = num % 10
    num = num // 10
    e = num % 10
    num = num // 10
    d = num % 10
    num = num // 10
    c =  num % 10
    num = num // 10
    b = num % 10
    num = num // 10
    a = num % 10
    return (a <= b and b <= c and c <= d and d <= e and e <= f) \
            and ( \
            (a == b and b != c) \
            or  (b == c and a != b and c != d) \
            or (c == d and b!=c and d != e) \
            or (d == e and c!=d and e!=f) \
            or (e == f and d!=e))
      
for i in range(sm, bg):
    if check_cond(i):
        total += 1
print(total)

