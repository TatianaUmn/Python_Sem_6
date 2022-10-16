# 1.	Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий
# делитель (НОД) двух чисел. Вычислите и напечатайте наибольший общий делитель
#  для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки. 

from math import gcd
 
list = []

while True: 
    num = input('Введите число: ')
    if num == '':
        break
    list.append(int(num))
print(list) # можно и не печатать, но так, мне кажется, нагляднее

res = gcd(list[0], list[1])
i = 2
for i in range(2, len(list)):
    res = gcd(res, list[i])
i += 1
print(res)
