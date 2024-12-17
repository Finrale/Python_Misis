# Средний бал и список отстающих учеников

grades = {
    "Иванов О.": 4,
    "Петров И.": 3,
    "Дмитриев Н.": 2,
    "Смирнова О.": 4,
    "Керченских В.": 5,
    "Котов Д.": 2,
    "Бирюкова Н.": 1,
    "Данилов П.": 3,
    "Аранских В.": 5,
    "Лемонов Ю.": 2,
    "Олегова К.": 4
}

total_grade = sum(grades.values())
average_grade = total_grade / len(grades)

failing_students = [student for student, grade in grades.items() if grade < 3]

print(f"Средний бал: {average_grade:.2f}")
print(f"Список отстающих учеников: {', '.join(failing_students)}")

# Посчитать количество определенных слов в файле

with open(r'C:\Users\snaki\OneDrive\Desktop\Понедельник.txt', 'r', encoding='utf-8') as file:
    content = file.read()

lec = content.count('лекц.')
pract = content.count('практ.')
lab = content.count('лаб.')

print('Лекций:', lec)
print('Практических:', pract)
print('Лабораторных:', lab)

# Откройте Telegram, найдите @BotFather и начните беседу. Отправьте команду /newbot и следуйте инструкциям.
# Finrale_bot


# Выведите список файлов в указанной директории. например где у вас лежат ваши тетради

import os

directory_path = r'C:\Users\snaki\Downloads\Telegram Desktop'

files = os.listdir(directory_path)

files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]

print("Список файлов в директории:", files)

# Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.

from collections import Counter
import re

text = """
Варкалось. Хливкие шорьки Пырялись по наве, И хрюкотали зелюки, Как мюмзики в мове.

О, бойся Бармаглота, сын! Он так свирлеп и дик! А в глу́ше ры́мит исполин — Злопастный Брандашмыг!

Но взял он меч, и взял он щит, Высоких полон дум. В глущобу путь его лежит Под дерево Тумтум.

Он стал под дерево и ждёт. И вдруг граахнул гром — Летит ужасный Бармаглот И пылкает огнём!

Раз-два, раз-два! Горит трава, Взы-взы — стрижает меч, Ува! Ува! И голова Барабардает с плеч!

О светозарный мальчик мой! Ты победил в бою! О храброславленный герой, Хвалу тебе пою!

Варкалось. Хливкие шорьки Пырялись по наве. И хрюкотали зелюки, Как мюмзики в мове.
"""

words = re.findall(r'\b\w+\b', text.lower())

# Находим наиболее часто встречающееся слово
word_counts = Counter(words)
most_common_word, most_common_count = word_counts.most_common(1)[0]

longest_word = max(words, key=len)

print(f"Наиболее часто встречающееся слово: '{most_common_word}' (встречается {most_common_count} раз)")
print(f"Самое длинное слово: '{longest_word}'")