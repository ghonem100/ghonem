import calc

print('-------------------------------')

print(calc.a)
calc.a = 10
print(calc.a)

import calc
print(calc.a)

print('-------------------------------')

from small import a, b

print(a)
print(b)

a = 20
b[0] = 15

print(a)
print(b)

import small

print(small.a)
print(small.b)
