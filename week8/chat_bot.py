import random

cities = {'msk': 'Москве', 'spb': 'Санкт-Петербурге'}
days = {'today': 'Сегодня', 'tomorrow': 'Завтра'}
w = [27, 14, 15, 11]
weathers = {}
count = 0
for city in cities:
    for day in days:
        weathers[(city, day)] = w[count]
        count += 1
            
def intent(s):
    for i in ['погода', 'градус', 'на улице']:
        if i in s:
            city, day = 'msk', 'today'
            for c in ['спб', 'питер', 'петербург']:
                if c in s:
                    city = 'spb'
            if 'завтра' in s:
                day = 'tomorrow'
            return 'weather', city, day
    for i in ['привет', 'здравствуй', 'добр']:
        if i in s:
            return 'hello'
    for i in ['пока', 'до свидан', 'спокойной']:
        if i in s:
            return 'goodbye'
    return None

def hello():
    return random.choice(['Привет!', 'Здравствуйте!', 'Добрый день!'])

def weather(city, day):
    return '{} в {} {} градусов тепла.'.format(days[day], cities[city], weathers[(city, day)])

def goodbye():
    return random.choice(['Пока!', 'До свидания!', 'До встречи!'])

def unknown():
    return random.choice(['Ммм.', 'Ну, такое.', 'Простите, я в этом не разбираюсь. :(', 'Если честно, я так себе собеседник.'])+' Давайте я лучше о погоде расскажу?'

def main():
    q = input().lower()
    while intent(q) != 'goodbye':
        if intent(q) is None:
            print(unknown())
        elif intent(q) == 'hello':
            print(hello())
        elif intent(q)[0] == 'weather':
            print(weather(intent(q)[1], intent(q)[2]))
        q = input().lower()
    else:
        print(goodbye())
        
main()
