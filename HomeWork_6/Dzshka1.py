
def speed(func):
    import time
    def wrapper(*args):
        t1 = time.time()
        res = func(*args)
        t2 = time.time()

        f = open('logs.txt', 'w')
        f.write('Вызвана: ' + time.ctime(t1) + '\n')
        f.write('Завершена: ' + time.ctime(t2) + '\n')
        f.write('Выполнялась: ' + str(int((t2 - t1)*1000)) + ' миллисекунд' + '\n')
        f.write('Значения на входе: ' + str([*args]) + '\n')
        f.write('Значения на выходе: ' + str(res) + '\n')

    return wrapper

@speed
def function(n, m):
    k = 0
    for i in range(n):
        for j in range(m):
            k += 1
    return k

function(100, 10000)
def simple_numbers(n):
    for i in range(1, n):
        simp = True
        for i1 in range(2, int(i**0.5)+1):
            if i % i1 == 0:
                simp = False
        if simp:
            yield i

for e in simple_numbers(1000):
    print(e)