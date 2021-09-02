1
list = ['Анна', 180, 50.5, True, None]
for i in list:
    print (type (i))

2
my_list = input('Напишите список').split()
my_list[:-1:2], my_list[1::2] = my_list[1::2], my_list[:-1:2]
print(my_list)

3
list  = ['зима', 'весна', 'лето', 'осень']
month = int(input('Введите номер месяца'))
if month == 1 or month == 2 or month == 12:
    print (list [0])
elif month == 3 or month == 4 or month == 5:
    print (list [1])
elif month == 6 or month == 7 or month == 8:
    print (list [2])
else:
    print (list [3])

month = int(input('Введите номер месяца'))
dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
if month == 1 or month == 2 or month == 12:
    print (dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print (dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print (dict.get(3))
else:
    print (dict.get(4))

4
str = input ('Напишите строку')
str1 = str.split()
for ind, el in enumerate (str1, 1):
    if len (el) > 10:
        el = el [0:10]
    print (ind, el)

5
my_list = [9, 7, 5, 4, 4]
n = int (input ('Введите число'))
for el in range (len (my_list)):
    if my_list [0]< n:
        my_list.insert(0, n)
        break
    else:
        if my_list [el] == n:
            my_list.insert(el + 1, n)
            break
        else:
            if my_list[el] > n and my_list [el+1] < n:
                my_list.insert(el + 1, n)
                break
            elif my_list [-1] > n:
                my_list.append(n)
print (my_list)

6
Извините, пока не смогла решить
