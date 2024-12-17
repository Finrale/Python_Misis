# Напишите функцию, извлекающую корень n-й степени из числа x. По умолчанию def будет извлекать квадратный корень:

def nth_root(x, n=2):
    if n <= 0:
        raise ValueError("Степень n должна быть положительным числом.")
    return x ** (1 / n)
x = int(input())

print(nth_root(x))

# Перепишите ваш код для проверки расширения из прошлого ДЗ в функцию которая принимает список расширений и имя файла

file = 'Моя диссертац.gif'
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

def check_extension(file_name):
    file_extension = file_name.split('.')[-1] #извлечение расширения файла из имени файла
    if file_extension.lower() in extensions:
        print(f"The file {file_name} has a valid extension.")
    else:
        print(f"The file {file_name} has an invalid extension.")

check_extension(file)

#Слейте воедино три словаря

def merge_dicts(dict_a, dict_b, dict_c):
    merged_dict = {**dict_a, **dict_b, **dict_c}
    return merged_dict

dict_a = {1: 10, 2: 20}
dict_b = {3: 30, 4: 40}
dict_c = {5: 50, 6: 60}

result = merge_dicts(dict_a, dict_b, dict_c)

print(result)

#Напишите функцию которая будет складывать цифры внутри числа

def sum(n):
    sum = 0
    while n > 0:
        a = n % 10
        sum = sum + a
        n = n//10
    return sum

n = int(input())
print(int(sum(n)))

#Нужно проверить, все ли числа в последовательности уникальны.

def are_numbers_unique(numbers):
    return len(numbers) == len(set(numbers))

numbers = [1, 4, 5]
result = are_numbers_unique(numbers)

if result:
    print("Все числа уникальны.")
else:
    print("Есть повторяющиеся числа.")

#Создать функцию, которая просто печатает все элементы заданного ей списка:

def print_list(my_list):
    for index in range(len(my_list)):
        print(f"НОМЕР {index} --> {my_list[index]}")
print_list(["я", "не", "в", "отпуск"])

