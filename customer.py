from order import Order
from coffee import Coffee
class Customer:
    def __init__(self,name):
        self.name =name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("DATA MUST BE A STRING")
        if not (1 <= len(value) <=15):
            raise ValueError("IT SHOULD BE BETWEEN 1 TO 15 CHARACTERS")
        
        self._name=value


    def orders(self):
        return [order for order in Order.all() if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        coffee_orders = [order for order in Order.all() if order.coffee == coffee]
        if not coffee_orders:
            return None

        customer_spending = {}
        for order in coffee_orders:
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price

        return max(customer_spending, key=customer_spending.get)

    @classmethod
    def all(cls):
        return cls._all
