class Order:
    _all_orders=[]

    def __init__(self,customer,coffee,price):
        from customer import Customer 
        from coffee import Coffee

        if not isinstance(customer,Customer):
         raise TypeError("It must be a Customer instance")
        if not isinstance(coffee,Coffee):
            raise TypeError("Must be a coffee instance")
        if not isinstance(price,float):
           raise TypeError("It must be a float")
        if not isinstance(1.0 <= price  <= 10):
           raise ValueError("Must be between 1 to 10 chararcters")

        self._customer=customer
        self._coffee=coffee
        self._price=price

        Order._all_orders.append(self)

        @property
        def customer(self):
           return self._customer
        
        @property
        def  coffee(self):
           return self._coffee
        
        @property
        def price(self):
           return self._price
        
        @classmethod
        def all(cls):
           return cls._all_orders
        