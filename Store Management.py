import csv
from item import Item
from phone import Phone
from Keyboard import Keyboard

item1= Item("Myitem",750)
item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)



"""While making a function inside a class, they are not called functions anymore, but methods instead"""

"""When making methods, the first parameter will always be itself, meaning the class we just made"""

"""When using OOP, a best practice its to ask for specific attributes when initializing an instance"""

"""Double underscore functions are called "Magic Methods" """

"""In case of using =0 while doing the init method, it means that the default value,the case where we dont pass
any paramenters on the """

# Dont call staticmethod or a classmethod from an instance, just call it from the class itselfb

# Input between () which class you would like to inherit from


#Since its inherited, you could use Phone instead of Item

#print(Item.__dict__)# Gives us all the attributes for the Class level
#print(item1.__dict__)# Gives us all the attributes for instance level


