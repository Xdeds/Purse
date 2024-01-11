# объект - единица инофрмации в памяти
# экземпляр - конкретный объект какого-то класса
# класс - инструкция по созданию объектов определенного типа
# метод - функция в классе на воздействия на объект
class Purse:
    def __init__(self, valuta, name='Unkown'):
        if valuta not in ('EUR', 'USD', 'SOM'):
            raise ValueError
        self.__money = 0.00  #Два нижних пробела до переменной означает приватность переменой,то есть за пределами класса мы никаким образом не сможем получить доступ к приватному объекту,только если мы не обозначим его одним лишь нижним пробелом
        self.valuta = valuta
        self.name = name
    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany
    def top_down_balance(self, howmany):
        try:
            if self.__money - howmany < 0:
                raise ValueError('Недостаточно средств на балансе')
            self.__money = self.__money - howmany
        except ValueError:
            print('Недастаточно средств на балансе, вывод невозможен')
        return howmany
    def info(self):
        return self.__money, self.valuta, self.name
    def __del__(self):
        print('Кошелек удалён')
x = Purse('EUR')
y = Purse('USD', 'Billy')
x.money = -100
y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))
# x.top_down_balance(12)
print(x.info())
print(y.info())


