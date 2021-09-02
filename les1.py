1
print ('добрый день')
age = 3
number = 9
name = 'Olga'
print (age)
print (number)
print (name)
weight = int (input ('введите массу'))
print (weight)
surname = input ('напишите фамилию')
print(surname)

2
seconds = int (input ('введите количество секунд'))
hours = seconds // 3600
minutes = seconds // 60
sec = seconds - hours*3600 - minutes*60
print (f"время {hours} : {minutes} : {sec}")

3
n = int (input ('введите число'))
nn = n*10 + n
nnn = n*100 + n*10 + n
print (n+nn+nnn)

4
n = int (input ('введите целое положительное число'))
max = n % 10
while n >= 0:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    else:
        print ('самая болшая цифра в числе', max)
        break

5
proceeds = float (input ('введите выручку фирмы'))
costs = float (input ('введите издержки фирмы'))
if proceeds > costs:
    print (f'выручка больше издержек, рентабельность составялет {proceeds / costs}')
    employers = int (input ('введите число сотрудников фирмы'))
    print(f'прибыль фирмы в расчете на одного сотрудника {proceeds / employers}')
else:
    print ('издержки больше выручки')

6
a = int (input ('введите расстояние пробежки в перввый день'))
b = int (input ('введите желаемое расстояние пробежки'))
day = 0
while a < b:
    a =a+a*0.1
    day = day +1
print (day)
