""" zad 1"""

"""x = int(input('введите число: '))
suma = 0
proizved = 1
while x > 0:
        ostatok = x % 10
        suma += ostatok
        proizved *= ostatok
        x = x//10
print("Сумма:", suma)
print("Произведение: ", proizved)"""

"""zad 2"""

"""x = int(input('введите число: '))
new = 0
while x > 0:
        ostatok = x % 10
        new*=10
        new +=ostatok
        x//=10
print("Новое число", new)"""

"""zad 3"""
"""x = int(input("Введите число: "))
chet = 0
nechet = 0
while  x > 0:
        if x%2==0:
                chet += 1
        else:
                nechet += 1
        x=x//10
print("Кол-во четных чисел: ", chet)
print("Кол-во нечетных чисел: ", nechet)"""

"""zad 4"""

"""x = int(input("Введите число: "))
factorial = 1
while x>1:
    factorial *= x
    x -= 1
print("Факториал введенного числа: ", factorial)"""

"""zad 5"""

from math import sqrt

n = int(input("введите число: "))
i = 2
while i <= sqrt(n):
    if n % i == 0:
        print("Составное число")
        break
    i += 1
else:
     print("Простое число")


