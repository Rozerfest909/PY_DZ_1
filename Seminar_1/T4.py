n = int(input())
# print(n > 5 or n > 9)
# Алгебра Логика
# True(1)
# False(0)
# n > 5 and n < 9
# and = *
# or = +
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('yes')
else:
    print('no')