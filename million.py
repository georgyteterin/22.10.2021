import random

bank = {
    'Франция': 'Париж',
    'Россия': 'Москва',
    'Украина': 'Киев',
    'Шри-Ланка': 'Коломбо',
    'США': 'Вашингтон',
    'Исландия': 'Рекъявик',
    'Гондурас': 'Тегусигальпа',
    }

countries = list(bank.items())
score = 0
number = 0

while number < 7:
    a = list(random.choice(countries))
    capital = a[1]  
    print(a[0])
    answer = str(input())
    if answer == capital:
        score += 1
        number += 1
        print('yeeep')
    else:
        number += 1
        print('nope')
print('results: ', score)
