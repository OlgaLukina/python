1
def my_div (arg_1, arg_2):
    return arg_1 / arg_2

arg_1 = int (input ('введите число'))
arg_2 = int (input ('введите число'))
if arg_2 !=0:
    print (my_div (arg_1, arg_2))
else:
    print ('на 0 делить нельзя')

2
def my_func (name, surname, birt, city, email, telephone):

    print(f"имя {name}; фамилия {surname}; год рождения {birt}; город {city}; почта {email}; телефон {telephone}")

my_func ('Anna', 'Ivanova', '1900', 'Moscow', 'ertyui', '789347895')

sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    print(sum(total))
my_func(-4, 2, 0)
3
def my_func(a, b, c):
    sps = [a, b, c]
    res_1 = max([a,b,c])
    sps.remove(res_1)
    res_2 = max(sps)
    result = res_1 + res_2
    return result
result = my_func(1, -2, 3)
print (result)

4
def my_func (x, y):
    result = 1 / (x ** abs(y))
    return result
result = my_func(1, -2)
print (result)

5
num = [1,2,3]
print(sum(num))
Дальше у меня не получается

6
def int_func(n):
    result = n.title()
    return result
result = int_func('ghjds')
print (result)

a = input ('введите слова')
print(int_func(a))






