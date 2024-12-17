# Задание 2
# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
import datetime

seconds=10000

def convert_seconds(seconds):
    return str(datetime.timedelta(seconds=seconds))

print(convert_seconds(seconds))

# Ответ: 2:46:40

# Напишите калькулятор который запрашивает на входе две переменные и знак, и в соответствии с знаком ( + - * / ) выводит результат
chislo1=input()
chislo2=input()
operation = input()

chislo1=int(chislo1)
chislo2=int(chislo2)

if operation == '+':
    print(chislo1+chislo2)
elif operation == '-':
    print(chislo1-chislo2)
elif operation == '/':
    print(chislo1/chislo2)
elif operation == '*':
    print(chislo1*chislo2)
else:
    print('Error!')

# Считайте 2 строки и выведите их на печать, разделив символом $.

string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

print(string1 + "$" + string2)

string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

print(string1, string2, sep="$")

# Напишите поздравление с Днем рождения, где программа считает имя и возраст и выведет поздравление столько раз, сколько лет именнинику

Name = input("Имя: ") + ","
Age = input("Возраст: ")
BirthdayText1 = "С днюхой тебя,"
BirthdayText2 = "c"
BirthdayText3 = "чем-то летием"

a=0
while (a<int(Age)):
    print(BirthdayText1, Name, BirthdayText2, Age, BirthdayText3)
    a+=1
print(a)

# Задание 3

# Какой месяц
month=1
m=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(m[month])
if (month!=0):
    print(m[month-1])

# Наибольший общий делитель
a=600
b=1012
i=b%a
while (i!=0):
    a=i
    i=b%a
print(a)

# Проверка расширения файла

file='Моя диссертац.gif'
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']
filename, file_extension = file.split('.')

if file_extension in extensions:
   print({file_extension})
else:
   print('Problem with extension')

# Вискосный год

year=2022
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('Високосный')
else:
        print('Невисокосный')