# Завдання 1
# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

import random

# def sum(ls:int):
#     sum=0
#     for element in ls:
#         sum+=element
#     return sum
#
#
# ls=[random.randint(1,10) for i in range(5)]
# print(ls)
# print(sum("Alex"))

# Завдання 2
# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

# import random
#
# def min_value(ls:int)->int:
#     return min(ls)
#
#
# ls=[random.randint(1,10) for i in range(5)]
# print(ls)
# print(min_value(ls))

# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

import random

# def simple_digit(ls)->int:
#     count=0
#     for digit in ls:
#       if digit >1:
#         flag=True
#         for i in range(2,digit):
#             if digit%i==0:
#                 flag=False
#                 break
#         if flag: count+=1
#     return count
#
#
# ls=[random.randint(1,10) for i in range(5)]
# print(ls)
# print(simple_digit(ls))
#
# Завдання 4
# Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість видаленних елементів.

# def delete_number(ls, number):
#     count=0
#     for i in ls:
#         if i==number:
#             ls.remove(i)
#             count+=1
#     return count
#
#
# ls=[random.randint(1,10) for i in range(5)]
# print(ls)
# number=int(input("Enter number to delete: "))
# print(delete_number(ls,number))


# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.

# import random
# def list_join(ls_1, ls_2):
#     ls_join=ls_1+ls_2
#     return ls_join
#
# ls_1=[random.randint(1,10) for i in range(5)]
# ls_2=[random.randint(1,10) for i in range(5)]
# print(ls_1)
# print(ls_2)
# print(list_join(ls_1, ls_2))


#
# Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр,
# список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.

# import random
#
# def degree_func(ls, degree_number):
#     ls_2=[]
#     for number in ls:
#         ls_2.append(number**degree_number)
#     return ls_2
#
# ls_1=[random.randint(1,10) for i in range(5)]
# print(ls_1)
# degree_number=int(input("Enter degree number: "))
# print(degree_func(ls_1, degree_number))
