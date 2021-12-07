#  *** Исключения (исключительные события, ситуации, ошибки) ***

# Пример исключения при делении на ноль
a = 100
b = 10

# отлов исключения
# try:
# # потенциально аварийный код
#     c = a / b
#     print("Все нормально ! :))")
# except:
# # код, который должен сработать при исключении
#     print("Что-то пошло не так :(")
#     c = 0

# print(c)


# Обработка множества исключений
# try:
#     a = int(input("Введите число: "))
#     result = 100 / a
#     # Конкретные классы исключений
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# except ValueError:
#     print("Нужно ввести число!")
    
#     # общее исключение
# except Exception as error:
#     print(error)

# Конструкция "try-except-finally"
# try:
#     a = int(input("Введите число: "))
#     result = 100 / a
#     print("Все нормально! :)")
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
#     result = 0
# finally:
#     print("Сработала finally")
#     result = 10

# print(result)


# Кастомизированные исключения 
# try:
#     a = input("Введите символ: ")
#     if a == 'A':
#         raise Exception("Ошибка А")
#     elif a == 'B':
#         raise Exception("Ошибка B")
#     elif a == 'C':
#         raise Exception("Ошибка C")
# except Exception as err:
#     print(err) 

# Пример приближенный к реальности
# while True:
#     try:
#         a = int(input("Введите число: "))
#         с = 100 / a
#     except ZeroDivisionError:
#         print("На ноль делить нельзя!")
#         continue
#     except ValueError:
#         print("Вы ввели не число!")
#         continue
#     print(f"Result: {c}")
#     break
    
#  Пример калькулятор
def calculate(n1, n2, op):
    d = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y,
        '**': lambda x, y: x ** y,
    }
    return d[op](n1, n2)

while True:
    # ввод данных
    cmd = input("Добрый день, пользователь: ")
    if cmd == "stop":
        print("Хорошего дня вам! ")
        break

    try:
        num_1 = int(input("Вводи 1 число: "))
        num_2 = int(input("Вводи 2 число: "))
        op = input("Ваши действия?: ")

        # обработка данных
        result = calculate(num_1, num_2, op)
    except ZeroDivisionError:
        result = "На ноль делить нельзя !"
    except ValueError:
        result = "Это не число !"
    finally:
        # вывод данных
        print(f"Результат: {result}")
    
    