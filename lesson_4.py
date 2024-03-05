# 1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку.
# Виведіть обидві кількості на екран. (використовувати цикл)

# custom_string=input("Enter some string: ")
# count_alpha =0
# count_num =0
# for i in custom_string:
#     if i.isalpha():
#         count_alpha+=1
#     if i.isdigit():
#         count_num+=1
# print(f"Count numbers is: {count_num}")
# print(f"Count letters is: {count_alpha}")

# 2. Користувач вводить з клавіатури рядок та символ для пошуку. Порахуйте скільки разів у рядку зустрічається потрібний символ.
# Отримане число виведіть на екран.

# custom_string=input("Enter some string: ")
# search=input("Enter a letter to search")
# count=0
# for letter in custom_string:
#     if search in letter:
#        count+=1
# print(count)

# 3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
# custom_string=input("Enter some string: ")
# search=input("Enter a word to search: ")
# letter_to_replace=input("Enter a word to replace: ")
# temp=custom_string.split()
# for i in range(len(temp)):
#     if temp[i]==search:
#         temp[i]=letter_to_replace
# print(temp:=' '.join(temp))


# 4. Дано рядок. (зробити зрізи)
# - Спершу виведіть третій символ цього рядка.
# - У другому рядку виведіть передостанній символ цього рядка.
# - У третьому рядку виведіть перші п'ять символів цього рядка.
# - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# - У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0,
# тому символи виводяться з першого).
# - У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
# - У сьомому рядку виведіть усі символи у зворотному порядку.
# - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
# - У дев'ятому рядку виведіть довжину цього рядка.
# Додатково:
# Є певний текст. Реалізуйте наступну функціональність:
# ■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;
# ■ Порахуйте скільки разів цифри зустрічаються у тексті;
# ■ Порахуйте скільки разів розділові знаки зустрічаються в тексті;
# ■ Порахуйте кількість знаків оклику в тексті.
# custom_string=input("Enter a string: ")
# print("The third symbol is: ", custom_string[2])
# print("Pre last symbol is: ", custom_string[-2])
# print("First five symbols is: ", custom_string[0:5])
# print("All except last two is: ", custom_string[0:len(custom_string)-2])
# print(custom_string)
# print("Paired numbers is: ")
# for letter in range(len(custom_string)):
#     if letter%2==0:
#         print (custom_string[letter], end="")
# print("\n")
# print("Odd numbers is: ")
# for letter in range(len(custom_string)):
#     if letter%2!=0:
#         print (custom_string[letter], end="")
# print("\n")
# print("Vise Versa string: ")
# for letter in range(len(custom_string)-1,-1,-1):
#         print (custom_string[letter], end="")
# print("\n")
# print("Vise Versa string skipped one: ")
# is_present=True
# count=0
# for letter in range(len(custom_string)-1,-1,-1):
#         if is_present:
#             print (custom_string[letter], end="")
#             count+=1
#         else: pass
#         is_present = not is_present
# print("\n")
# print("Length of that string is: ", count)

#■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;
# custom_string=input("Enter a string: ")
# print(custom_string.title())

#Порахуйте скільки разів цифри зустрічаються у тексті;
# custom_string=input("Enter a string: ")
# count=0
# for letter in custom_string:
#     if letter.isdigit():
#         count+=1
# print(count)

