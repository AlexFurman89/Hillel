# Важливо: не використовувати цикли для реалізації основної логіки.
# Потрібно використати рекурсію.
# Цикл можна використовувати лише у 4 завданні для знаходження суми чисел.
#
################
# Завдання 1.
# Написати рекурсивну функцію знаходження ступеня числа.
# def my_pow(number, power):
#     if power <= 1:
#         return number
#
#     return number * my_pow(number, power - 1)
# print(my_pow(2, 3))

# my_pow(2, 3) -> 2 * my_pow(2, 2) => 8
# my_pow(2, 2) -> 2 * my_pow(2, 1) => 4
# my_pow(2, 1) => 2

# Завдання 2.
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)
# def stars (number_of_stars):
#     if number_of_stars <= 1:
#         return " * "
#     return " * " + stars(number_of_stars-1)
#
# number_of_stars=int(input("Number of stars: "))
# print(stars(number_of_stars))

#stars(3) -> "*" + stars(2)
#stars(2) -> "*" + stars(1)
#stars(1) -> *
# Завдання 3.
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.

def sum_of_elements(a,b)->int:
    swap=[a,b]
    if a > b:
        swap = [b,a]
    new_list=list(range(swap[0],swap[1]+1))
    print(new_list)
    sum=0
    for _ in new_list:
        sum+=_
    return sum
a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
print(f"Sum of elements is {sum_of_elements(a,b)}")


# Додатково:
# Завдання 4.
# Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим чином і знаходить позицію,
# з якої починається послідовність із 10 чисел, сума яких мінімальна.
########
##########


