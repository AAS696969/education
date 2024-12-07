num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

message = '''
Выберете математическую операцию:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение

Ваш выбор:
'''

# спрашиваем у пользователя, какую операцию он хочет выбрать
operation = input(message)

# выводим выбранную операцию (или сообщение об ошибке)
if operation == "+":
     res = num1 + num2
elif operation == "-":
    res = num1 - num2
elif operation == "/":
    try:
        res = num1 / num2
    except ZeroDivisionError:
        res = ("NUM2=0, деление на ноль невозможно")
elif operation == "*":
    print('Умножение')
    res = num1 * num2
else:
    print('Неизвестная операция')
print(res)