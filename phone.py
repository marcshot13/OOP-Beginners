import csv
from item import Item

class Phone(Item):
    #call super function to call all the attributes and methods from parent class

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name,price,quantity)
        #We can use assert to run validations to the received arguments
        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater or equal to zero"

        #Assing to self object
        self.broken_phones = broken_phones

    pass
