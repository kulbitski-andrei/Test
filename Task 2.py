# Напишите 2 функции:
# Которая запрашивает у пользователя число и выводит его квадрат
# Которая запрашивает у пользователя число и определяет, является ли оно четным или нечетным

def num_expo(x):
    return x * x


def even_odd(y):
    if y % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(num_expo(5))
print(even_odd(1))
print(even_odd(2))
