import datetime


now = datetime.datetime.now()  # текущее время в переменной
print(f'Полное время сейчас: {now}')
print(f'Сегодняшняя дата: {now.date()}')
midnight = datetime.datetime.now().replace(
    hour=0,
    minute=0,
    second=0,
    microsecond=0
)  # текущая дата без date()
print(f'Разница между сейчас и полночью: {now - midnight}')
print(f'Прибавляем к текущему времени 15 часов: {now + datetime.timedelta(hours=15)}')
print(f'Текущий час: {now.hour}')
