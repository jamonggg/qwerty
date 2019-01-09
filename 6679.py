#6679.py
def t(n):
    result = 0
    while n != 0:
        result = result + int(n % 10)
        n = int(n/10)
    return int(result)
def tw(n):
    result = 0
    while n != 0:
        result = result + int(n % 12)
        n = int(n/12)
    return int(result)
def ts(n):
    result = 0
    while n != 0:
        result = result + int(n % 16)
        n = int(n/16)
    return int(result)

for i in range(1000,10000):
    if t(i) == tw(i) and t(i) == ts(i):
        print(i)
