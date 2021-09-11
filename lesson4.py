1
from sys import argv
working_out, bid, prize = argv
calculation = (int(working_out)*int(bid)+int(prize))
print (calculation)
2
my_list =[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for num, el in enumerate(my_list) if my_list [num-1]< my_list[num]]
print (new_list)

3
my_set = {el for el in range (20, 241) if el%20==0 or el%21==0}
print (my_set)

4
my_list =[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el)==1]
print (new_list)

5
from functools import reduce
my_list = [el for el in range [99, 1001] if el%2==0]
def my_func(prev_el, el):
    return prev_el * el

print (reduce (my_func, my_list))

6
from itertools import count
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle

с = 0
for el in cycle("ABC"):
    if с > 9:
        break
    print(el)
    с=c+1

7
from itertools import count
from math import factorial

def fact ():
    for el in count (1):
        yield factorial(el)

f=fact()
c=0
for i in f:
    if c<4:
        print (i)
        c=c+1
    else:
        break
