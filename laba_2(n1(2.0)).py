import math
x = float(input("Введите x (x < -1): "))
n = int(input("Введите n: "))

s = -math.pi/2
xrazr = x
steps = 0
for n in range(1000):
    v = (-1) ** (n+1) / ((2 * n + 1) * xrazr)
    s += v
    steps += 1
    xrazr *= x * x
    if abs(v) < n:
        break
print('сумма ряда: ', s)
print('кол-во шагов: ', steps)

v= -math.pi/2 
g = 0
for q in range(n):
    v = v + (-1) ** (q+1)/((2*q+1)*x**(2*q+1))
    g += v
print ('сумма ряда не опт вариант =', g)
