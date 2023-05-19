# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

x = int(input("Введите номер билета из 6 символов > "))
a = x // 100000 + x // 10000 % 10 + x // 1000 % 10
b = x // 100 % 10 + x // 10 % 10 + x % 10

if len(str(x)) == 6:
    if a == b:
        print("Это число счастливое")
    else:
        print("Это число не счастливое")
else:
    print("Это число не из шести символов")