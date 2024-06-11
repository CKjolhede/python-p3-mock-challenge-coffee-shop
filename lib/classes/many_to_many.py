class Coffee:
    
    all = []

    def __init__(self, name):
        self._name = name
        self.__class__.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, value):
        if (type(value)) == "str" and len(value) >= 3:
            self._name = value
        else:
            return self._name
    
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        customer_set = {(order.customer) for order in self.orders()}
        return list(customer_set)

    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum(order.price for order in self.orders())/self.num_orders()

class Customer:
    
    all = []
    
    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else: 
            raise TypeError("Name must be a string with 1 to 25 characters")
        return
    
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        coffee_types_ordered = {order.coffee for order in self.orders()}
        return list(coffee_types_ordered)
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)       
    
class Order:
    
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = float(price)
        self.__class__.all.append(self)
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0 and not hasattr(self, "price"):
            self._price = price
        return
    