class Product():

    def __init__(self, id=0, name=' ', stock=0, cost=0.0):
        self._id = id
        self._name = name
        self._stock = stock
        self._cost = cost


    def __str__(self):
        return f'{self._id}-{self._name}: stock-{self._stock}, cost-{self._cost}'

    @property
    def id (self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name (self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def stock (self):
        return self._stock
    @stock.setter
    def stock(self, stock):
        self._stock = stock

    @property
    def cost (self):
        return self._cost
    @cost.setter
    def cost(self, cost):
        self._cost = cost

if __name__ == '__main__':
   product_1 = Product(name = 'Rice', stock=20, cost=2)

   print(product_1)
        