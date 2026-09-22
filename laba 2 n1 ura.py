from math import pi

x = float(input("Введите x (x < -1): "))
n = int(input("Введите целое число n > 0: "))

if x >= -1 or n <=0:
    print('введены неверные значения')
    exit()
steps = 0
v = 0
xrazr = x
znak = 1
xx = x * x

for b in range(n):
    v += znak / ((2 * b + 1) * xrazr)
    steps += 1
    znak = -znak
    xrazr *= xx

s = -pi / 2 + v

print("Оптимизированный вариант: ", s)

# неопт вариант
d = -pi / 2

for q in range(n):
    d += (-1) ** q / ((2 * q + 1) * x ** (2 * q + 1))

print("не оптимизированный вариант: ", d)

print("кол-во шагов:  ", steps)