import math
x = float(input("Введите x (x < -1): "))
n = int(input("Введите n: "))

s = -math.pi/2
xrazr = x
steps = 0
for n in range(1000):
    v = (-1) ** (n+1) / ((2 * n + 1) * xstep)
    s += v
    steps += 1
    xrazr *= x * x
    if abs(v) < n:
        break
print('сумма ряда: ', s)
print('кол-во шагов: ', steps)