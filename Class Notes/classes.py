'''class product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_quantity(self):
        return self.__quantity
    
    def set_name(self, name):
        self.__name = name
    def set_price(self, price):
        self.__price = price
    def set_quantity(self, quantity):
        self.__quantity = quantity

item = product('car',1,1)'''


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