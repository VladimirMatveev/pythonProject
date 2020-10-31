from hage.Multiply import Main4
from hage.Minus import Main2
from hage.Plus import Main1
from hage.Division import Main3





class Main(Main1,Main2,Main3,Main4):
    def __init__(self, q1, q2, v):
        self.q1 = q1
        self.q2 = q2
        self.v = v


    def show(self):
        vvod = (self.q1 + self.q2 + self.v)
        print(vvod)


myclass = Main(int (input('Введите число 1: ')),
               int (input('Введите число 2: ')),
               int(input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n')))

myclass.condition()
myclass.condition2()
myclass.condition3()
myclass.condition4()