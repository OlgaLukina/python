1
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def my_method(cls, day_month_year):
        my_data = []
        for i in day_month_year.split():
            if i != '-': my_data.append(i)
        return int (my_data[0]), int(my_data[1]), int (my_data[2])

    @staticmethod
    def valid(day, month, year):
        if 1<=day<=31 and 1<=month<=12 and 0<=year<=2021:
            return f'дата верна'
        else:
            return f'дата указана неверно'

today = Data('20 - 09 - 2021')
print (today)
print(today.my_method('20 - 09 - 2021'))
print(today.valid(20, 9, 2021))
print(today.valid(20, 14, 2021))

2
class ZeroDivisionError:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    def divid(self):
        if self.divider == 0:
            print ('На ноль делить нельзя')
        else:
            return (self.dividend/self.divider)

abc = ZeroDivisionError (12, 3)
cds = ZeroDivisionError (12, 0)
print(abc.divid())
print(cds.divid())

3
class Exception:
    def __init__(self, *args):
        self.list = []

    def my_func(self):
        while Truue:
            try:
                abc = input('введите элемент')
                if abc == 'stop':
                    break
                elif type(abc) is int:
                    self.list.append(abc)
                    print (self.list)
                else:
                    print ('ввели недопустимый элемент')

asd = Exception()
print (asd.my_func())

4
class Office_equipment:
    def __init__(self, name, number,amount,years):
        self.name=name
        self.number=number
        self.amount=amount
        self.years=years

    def __str__(self):
        return (f'{self.name}, номер {self.number}, количество {self.amount}, срок {years}')

    @property
    def inp(self):
        try:
            abc = input ('введите название')
            abc_a= int(input('введите количество'))
            abc_y= int(input('введите срок'))
            print ({'название':abc, 'количество':abc_a, 'срок':abc_y})
        except:
            return ('неправильно введены данные')

class Printer (Office_equipment):
    def print(self):
        return (f'напечатать на принтере {self.number}')

class Scanner (Office_equipment):
    def scan(self):
        return (f'отсканировать на сканере {self.number}')

class Copier (Office_equipment):
    def copi(self):
        return (f'сделать копии на ксероксе {self.number}')

a=Printer('Sumsung', 90, 5, 2000)
b=Scanner('Philips', 803, 8, 2005)
c=Copier('Tosh', 123, 10, 2007)
print(a.inp())
print(b.scan())
print(c.copi())

5
class Complex_number:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return (self.x * other.x, self.y * other.y)

a = Complex_number(2, 4)
b = Complex_number(1, 10)
print(a+b)
print(a*b)

