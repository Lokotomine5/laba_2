from math import pi
x = float(input("Введите x (x < -1): "))
if x >= -1:
    print('введите x < -1')
    exit()
n = int(input("Введите целое число n > 0: "))
if n <= 0:
    print('введите другое число n')
    exit()

s = -pi/2
xrazr = x
steps = 0
for b in range(n):
    v = (-1) ** (b+1) / ((2 * b + 1) * xrazr)
    s += v
    steps += 1
    xrazr *= x * x

print('сумма ряда: ', s)
print('кол-во шагов: ', steps)

d= -pi/2
for q in range(n):
    h = (-1) ** (q+1)/((2*q+1)*x**(2*q+1))
    d += h
print ('сумма ряда не опт вариант =', d)
