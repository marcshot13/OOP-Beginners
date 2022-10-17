import csv

class Item:

    pay_rate = 0.8 #Its inside the class but not the instance
    all = []

    #To specify which datatype to use in every attribute, we can use :(datatype) to tell which datatype is to be used
    #in. When typing quantity =0, i tell the attribute also to be always an int

    def __init__(self, name: str, price: float, quantity=0):

        #We can use assert to run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"


        #Assing to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity


        #Actions to execute
        Item.all.append(self)

    #Property makes the attribute read only
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate # We use item. because its not inside the instance, but inside the class

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        return self.price*self.quantity


    @classmethod
    def instantiate_from_csv(cls):
        with open('Datos.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price= float(item.get('price')),
                quantity= float(item.get('quantity')))

    @staticmethod
    def is_integer(num):
        #We will convert the point zero float numbers into integers
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"

    pass