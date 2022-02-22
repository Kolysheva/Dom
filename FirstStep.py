name = "Polina"
print(name)
age = "18"
print('Hello, my name is', name, 'and my age is', age)
povtor = (name+name*4)
print(povtor)

user_name = input('Как вас зовут?')
if ' ' in user_name:
    print('Напишите имя без пробелов')
    exit()

user_age = input('Сколько вам лет?')
try:
    user_age_int = int(user_age)
    if user_age_int < 0:
        print ('Привет ' + user_name + ', кажется ты еще даже не родился... Твое время еще придет.')
        exit()
    elif user_age_int > 150:
        print('Привет ' + user_name + ', рада вас видеть, но вам не сюда надо, а в книгу рекордов.')
        exit()
    elif user_age_int > 70:
        print('Привет ' + user_name + ', рада вас видеть, но перед занятием выпейте таблетки!')
    elif user_age_int > 7:
        print('Привет ' + user_name + ', кажется вы пришли вовремя')
    else:
        print('Привет ' + user_name + ', рада видеть тебя, но сначала надо выучить таблицу умножения :с')
except ValueError:
    print('Кажется вы написали слово... Используйте пожалуйста цифры.')

print(user_name[1:][:-1])
print(user_name[-3:])
print(user_name[:5])
print(user_name[::-1])

width_name = len(user_name)
print(width_name)

try:
    summa = int(user_age[0]) + int(user_age[1])
    print(summa)
except IndexError:
    summa = int(user_age[0]) + 0
    print(summa)

try:
    umnosenie = int(user_age[0]) * int(user_age[1])
    print(umnosenie)
except IndexError:
    umnosenie = int(user_age[0]) * 0
    print(umnosenie)
    #К примеру 9 лет = 9.0


print(user_name.upper())
print(user_name.lower())
print(user_name.capitalize())
perevernutoe = (user_name.capitalize())
print(perevernutoe.swapcase())

zadacha = input('Решите пожалуйста задачу\n 2^0+2-2=??')
if int(zadacha) == 1:
    print('Молодец!')
else:
    print('Кажется надо обратить внимание на внимательность')