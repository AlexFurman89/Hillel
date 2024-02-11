# 1. Користувач вводить три цифри з клавіатури. Залежно від вибору користувача програма
# виводить на екран
# максимум із трьох, мінімум із трьох або середньоарифметичне трьох чисел.
#Task:

numbers = []
while True:
    numbers.append(int(input("Enter Number: ")))
    if len(numbers) == 3:
        break
print(f"max value: {max(numbers)}")
print(f"min value: {min(numbers)}")
avg_value = sum(numbers)/len(numbers)
print(f"max value: {avg_value}")
