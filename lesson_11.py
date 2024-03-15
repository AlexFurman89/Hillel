# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер

# SOURCE_FILE="test.txt"
# TARGET_FILE="test_2.txt"
# WORD_LEN=7
#
# with open(SOURCE_FILE, 'w',encoding='utf-8') as source_file:
#     source_file.write(input("Enter some texts: "))
# with open(SOURCE_FILE,'r',encoding='utf-8') as source_file:
#     result=source_file.read()
# print(result)
# splitted_result=result.split()
# print(splitted_result)
#
# with open(TARGET_FILE, 'w', encoding='utf-8') as target_file:
#     for word in splitted_result:
#         if len(word)>=WORD_LEN:
#             target_file.write(f"{word} ")
# with open(TARGET_FILE, 'r', encoding='utf-8') as target_file:
#     print(result, end=' ')


# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.

# SOURCE_FILE="test.txt"
# count=0
# with open(SOURCE_FILE, 'r', encoding='utf') as s_file:
#     result=s_file.read()
# print(result)
# result_splitted=result.split()
# print(len(result_splitted))
# 3. Створіть програму, яка перевіряє текст на неприпустимі слова.
#
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
#
# За підсумками роботи програми необхідно показати статистику дій.
#
# Наприклад, якщо й у нас є такий текст:


list_with_abused_words=[]
count=0
while True:
    abused_word=input("Enter abused word OR ""c"" to check the input text file: ")
    if abused_word =="c": break
    else: list_with_abused_words.append(abused_word)

SOURCE_FILE="test.txt"
with open(SOURCE_FILE, 'r', encoding='utf') as s_file:
    result=s_file.read().split()
for word in range(len(result)):
    if result[word] in list_with_abused_words:
        result[word]='...'
        count+=1
print(result)
print("number of abused_words= ",count)
