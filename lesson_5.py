# users=["Alex","Roma","Vasya"]
# user_1,user_2,user_3=users
# print(user_1)
# print(user_2)




# Завдання 1
#
# У списку цілих, заповненому випадковими числами обчислити:
# ■ Суму негативних чисел;
# ■ Суму парних чисел;
# ■ Суму непарних чисел;
# ■ Добуток елементів з кратними індексами 3;
# ■ Добуток елементів між мінімальним та максимальним елементом;
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.

# import random
# random_digits = [random.randint(-10, 10) for i in range(10)]
# negative_sum=0
# paired_sum=0
# index_sum=0
# for digit in random_digits:
#     if digit<0: negative_sum+=digit
#     if (digit%2==0): paired_sum+=digit
# for index in range(len(random_digits)):
#     if (index%3==0): index_sum*=random_digits[index]
# print(random_digits)
# print(negative_sum)
# print(index_sum)
# print(min(random_digits)*max(random_digits))
# count=0
# slice=[]
# for name in range(len(random_digits)):
#     if random_digits[name] > 0:
#         slice.append(name)
#         count+=1
#         if count ==2: break
# print(slice)
# new_list=random_digits[slice[0]:slice[1]+1]
# print("Old list: ", random_digits)
# print("New list: ", new_list)
# print(sum(new_list))

# Завдання 2
#
# Є список цілих, заповнений випадковими числами.
# На підставі даних цього масиву потрібно:
# ■ Створити список цілих, що містить лише парні числа з першого списку;
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.
# Додаткові завдання по матрицях (надіслати як завжди мені в лс після виконання основного дз):
# створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
# вивести на екран
# - вивести суму чисел головної діагоналі матриці
# - вивести мінімальне та максимальне значення побічної діагоналі матриці
# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# (аналогічно зробити з рядком)

import random
random_digits = [random.randint(-10, 10) for i in range(10)]
paired_random_digits=[]
odd_random_digits=[]
negative_random_digits=[]
positive_random_digits=[]
for digit in random_digits:
    if digit%2==0: paired_random_digits.append(digit)
    else: odd_random_digits.append((digit))
print(random_digits)
print(paired_random_digits)
print(odd_random_digits)
for digit in random_digits:
    if digit <0: negative_random_digits.append(digit)
    else: positive_random_digits.append(digit)
print(negative_random_digits)
print(positive_random_digits)