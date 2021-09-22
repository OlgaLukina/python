1
class Matrix:
    def __init__(self, list1, list2):
        self.list1=list1
        self.list2=list2

    def __add__(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        for i in range (len(self.list1)):
            for j in range (len(self.list2)):
                matrix [i][j]=self.list1[i]+self.list2[j]
                return str (matrix)

my_matrix = Matrix ([[1, 3, 5],
                     [2, 5, 15],
                     [43, 22, 4]],
                    [[4, 7, 9],
                    [17, 8, 5],
                    [1, 14, 22]])

print (my_matrix.__add__())


2
class Clothes:
    def __init__(self, size, height):
        self.size=size
        self.height=height

    @property
    def cons_gen(self):
        return (self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)

class Coat (Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def cons_s(self):
        return self.size/6.5 + 0.5

class Jacket (Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def cons_h(self):
        return self.height*2 + 0.3



coat = Coat (42, 170)
jacket = Jacket (42, 170)
print (coat.cons_s())
print (jacket.cons_h())
print (jacket.cons_gen)

3
class Cell:
    def __init__(self, numbers):
        self.numbers=int(numbers)

    def __add__(self, other):
        return self.numbers + other.numbers

    def __sub__(self, other):
        if self.numbers>other.numbers:
            return self.numbers-other.numbers
        else:
            return other.numbers-self.numbers

    def __mul__(self, other):
        return self.numbers * other.numbers

    def __truediv__(self, other):
        return self.numbers / other.numbers

    def __make_order__(self, in_row):
        return self.numbers/in_row

c1=Cell(20)
c2=Cell(25)
print (c1+c2)
print (c1-c2)
print (c1*c2)
print (c1/c2)
print (c1.__make_order__(2))
print (c2.__make_order__(3))







