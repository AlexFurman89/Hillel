# 1. Користувач вводить три цифри з клавіатури. Залежно від вибору користувача програма
# виводить на екран
# максимум із трьох, мінімум із трьох або середньоарифметичне трьох чисел.

# numbers = []
# while True:
#     numbers.append(int(input("Enter Number: ")))
#     if len(numbers) == 3:
#         break
# print(f"max value: {max(numbers)}")
# print(f"min value: {min(numbers)}")
# avg_value = sum(numbers)/len(numbers)
# print(f"max value: {avg_value}")


# 2. Користувач вводить з клавіатури кількість метрів.
# Залежно від вибору користувача програма переводить метри милі,
# дюйми або ярди.

meters=int(input("Enter meters: "))
choice=int(input("1-meters->miles; 2-meters->inches; meters->yards: "))
if choice==1:
    miles=meters*0.000621371
    print(miles)
if choice==2:
    inches=meters*39.37
    print(inches)
if choice==3:
    yards=meters*1.09361
    print(yards)