# 1. Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.
# try:
#     while True:
#         day_of_week = int(input("Enter a day of the week: "))
#         match day_of_week:
#             case 0:
#                 break
#             case 1:
#                 print("Monday")
#             case 2:
#                 print("Tuesday")
#             case 3:
#                 print("Wednesday")
#             case 4:
#                 print("Thursday")
#             case 5:
#                 print("Friday")
#             case 6:
#                 print("Saturday")
#             case 7:
#                 print("Sunday")
#             case _:
#                 print("Please enter between 1 and 7")
# except ValueError as error:
#     print("Enter only integer numbers please. Day of the week: {1-7}!")
# finally:
#     print("End of execution")




# 2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання
# try:
#     number_1=int(input("Enter the first number: "))
#     number_2=int(input("Enter the second number: "))
#     if number_1==number_2:
#         print("Numbers are equal")
#     if number_1>number_2:
#         print(f"{number_1}, {number_2}")
#     if number_1<number_2:
#         print(f"{number_2}, {number_1}")
# except ValueError:
#     print("Enter only integer values")

# 3. Користувач вводить два числа та матем дію: + - * або /
try:
    number_1=int(input("Enter the first number: "))
    number_2=int(input("Enter the second number: "))
    choice=input("Expect action: +, -, *, /: ")
    match choice:
        case "+":
            print(f"Number 1 + Number 2 ={number_1+number_2}")
        case "-":
            print(f"Number 1 - Number 2 ={number_1 - number_2}")
        case "*":
            print(f"Number 1 * Number 2 ={number_1 * number_2}")
        case "/":
            print(f"Number 1 / Number 2 ={number_1 / number_2}")
except ValueError:
    print("Enter only integer values")

