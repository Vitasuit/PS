#리스트 컴프리헨션
a = [n*2 for n in range(1,10+1) if n % 2 ==1 ]
print(type(a))
print(a)

#리스트 컴프리헨션 미사용

b = []
for n in range(1, 10 +1):
    if n % 2 == 1:
        b.append(n * 2)

print(type(b))
print(b)

#딕셔너리 컴프리헨션
c = {}
for key, value in c.items():
    c[key] = value
print(type(c))
print(c)

#제너레이터
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

g = get_natural_number()
for _ in range(0,100):
    print(next(g))

def generator():
    yield 1
    yield 'string'
    yield True

g = generator()
print(next(g))
print(next(g))
print(next(g))


