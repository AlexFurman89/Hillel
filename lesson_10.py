# Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
# - домашній номер телефону (тільки цифри та довжина номера)
# import re
# home_number = input("Enter your home number: ")
# if re.search(r'.*\d{7}.*', home_number) and len(home_number)==7:
#     print("This is a home number")
# else:print("This is NOT a home number")

# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# import re
# mobile_number = input("Enter your mobile number: ")
# if re.search(r'\+?380\d{9}', mobile_number) and len(mobile_number) == 13:
#     print("This is a mobile number")
# else:
#     print("This is NOT a mobile number")

# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
# import re
# email = input("Enter your email: ")
# if re.search(r'^[a-zA-Z0-9]+@gmail.com$', email) and len(email) >= 11:
#     print("This is a valid email")
# else:
#     print("This is NOT a valid email")

# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
import re
first_last_middle_name = input("Enter your First Last Middle name: ")
check_input=first_last_middle_name.split()
counter=0
if len(check_input)==3:
    for name in check_input:
        if re.search(r'[a-zA-Z]+', name) and len(name)>=2 and len(name) <=20:
            counter+=1
if counter==3: print("Valid")
else:print("Invalid")
