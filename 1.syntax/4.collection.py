#   ***  Коллекции  ***
 
# Список (list)

# создание пустого списка 
my_list = []
my_list = list()

# создание предварительно наполненного списка
my_list = [1, 2, 3, 4, 5, "python", 3,14, [1,2,3]]

# добавление объекта (элемента) в список 
my_list = []

my_list.append(100)
my_list.append(2.5)
my_list.append("Hello")
my_list.append([10,20,30])

# чтение значений элемента списка 
# прямая индексация (слева направо)
el = my_list[0]
el = my_list[3]

# чтение значений вложенных коллекций 
el = my_list[2][1]

# обратная индексация
el = my_list[-1]

# замена значений
my_list[-1] = 777.0

# удаление элемента по значению
my_list.remove(2.5)

# удаление элемента по индексу
del my_list[-1]

# print(my_list)
# print(el)


# срез списка 

# создание исходного списка из строки 
s = "Hello World!"
my_list = list(s)

# срез от начала до конца
my_slice = my_list[:]

# срез от второго индекса до конца исходного списка
my_slice = my_list[2:]

# срез с начала списка до 5-го индекса не включительно
my_slice = my_list[:5]

# срез с 3-го индекса до 7-го индекса не включительно
my_slice = my_list[3:7]

# срез от начала до конца списка с шагом 2
my_slice = my_list[::3]

# срез с 3-го индекса до 9-го с шагом 2 
my_slice = my_list[3:9:2]

# срез с -2-го индекса до -9 с шагом 2
my_slice = my_list[3:9:2]

# переворот списка срезом
my_slice = my_list[::-1]

# print(my_list)
# print(my_slice)

# длина - число элементов в объекте
print(len(my_list))


#  *** Кортеж (tuple) ***

# неизменяемая (immutable)
# легковеснее, чем список

# создание кортежа
my_tuple = (10, 20, 30, 40)

# чтение значений
el = my_tuple[0]

# срез из кортежа
my_slice = my_tuple[2:]

# print(my_tuple)
# print(my_slice)


#  *** Словарь (dict) ***

# пара "ключ-значение"
# {ключ_1:значение_1, ключ_2:значение_2}

# создание словаря 
my_dict ={10:3.14,"abc":[1,2,3], 'A':"python"}

# чтение значений
val = my_dict["abc"]

# замена значения
my_dict[10] = 1000

# добавление новой пары
my_dict["hi"] = "hello"

# удаление пары по ключу
del my_dict["A"]

print(my_dict)
# print(val)

# множество (set)
# неупорядоченная коллекция уникальных элементов

# создание
a = {1,2,3,1,2,3,1,2,3,4}

b = {'hi, ha, hi, ha, ho'}

c = set ('abracadabra')
print(c)