class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def quantity(self,value):
        if 0 <= value <= 99:
            self.quantity = value

    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_quantity(self):
        return self.quantity
    
    def set_name(self, name):
        self.name = name
    def set_price(self, price):
        self.price = price
    def set_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'The product is {self.__name} and price is {self.__price}. We have {self.__quantity}'
appleiphone = product('iphone17', 1499, 1)
car = product('car',2000,1)



#5
class Employee:
    def __init__(self, name, title, salary):
        self.__name = name
        self.__title = title
        self.__salary = salary

    def get_name(self):
        return self.__name
    def get_title(self):
        return self.__title
    def get_salary(self):
        return self.__salary
    
    def set_name(self, name):
        self.__name = name
    def set_title(self, title):
        self.__title = title
    def set_salary(self, salary):
        self.__salary = salary

    def greeting(self):
        return f'hello, my name is {self.__name}, I am the {self.__title} '