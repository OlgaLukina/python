1
f_1 = open ('my_file1.txt', 'w')
while True:
    str_list = input('введите текст')
    f_1.writelines(str_list)
    if not str_list:
        break

f_1 = open ('my_file1.txt', 'r')
content = f_1.readlines()
print (content)
f_1.close()

2
text = open ('my_file1.txt', 'r')
num_str = text.readlines()
print ({len (num_str)})
for line in 'my_file1.txt':
    words = len(line)
    print (words)

3
#Почему то не выходит посчитать среднее
from statistics import mean
value = []
with open('file2.txt', 'r') as my_file:
    for line in my_file:
        key, value = line.split()
        if int(value) < 20000:
            print (f'{key}')
print (mean (map(int, value)))

4
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
result = []
with open ('file4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' — ', 1)
        result.append(translate [i[0]] + ' — ' + i[1])
        print(result)

5
f_5 = open ('file5.txt', 'w')
list = input('введите числа')
f_5.writelines(list)
num = list.split()
print (sum(map(int, num)))

6
result = {}
f_6 = open ('file6.txt', 'r')
for line in f_6:
    subj, lec, prac, lab = line.split()
    result [subj] = int(lec)+int(prac)+int(lab)
print (f'\n {result}')

7
import json
profit = {}
aver = 0
meanaver = 0
i=0
with open ('file7.txt') as file_obj:
    for line in file_obj:
        print(line)
        name, form, earn, cost = line.split()
        profit [name] = int(earn) - int(cost)
        if profit [name]>0:
            aver = aver + profit [name]
            i=i+1
    meanaver = aver / i
    print (f'Средняя прибыль {meanaver}')
    print (f'Прибыль каждой компании - {profit}')

with open ('file7.txt', 'w') as write_f:
    json.dump (profit, write_f)
    json_str=json.dumps (profit)
print (json_str)