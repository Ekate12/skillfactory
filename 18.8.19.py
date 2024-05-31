s = 0
n=int(input('Введите количество билетов: '))
for age in range (n):
    age=int(input('Введите возраст посетителя: '))
    if age < 18:
        print('Билет бесплатный')
    elif age > 25:
        s+=1390
    else:
        s += 990
if n>3:
    a=0.9
else:
    a=1
print ('Стоимость Ваших билетов: ', s*a)