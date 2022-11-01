"""Example of a class and object instantiation."""


from ctypes import sizeof
from typing_extensions import Self


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute Definitions
    size: str
    toppings: int
    extra_cheese: bool
    
    def __init__(self, size: str, toppings: int):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings


    def price(self, tax: float) -> float:
        """Calculate the price of a pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
        total += self.toppings * 0.75
        if self.extra_cheese:
            total += 1.0
        total *= tax
        return total

a_pizza: Pizza = Pizza("Large",3) #Constructor Call
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False
print(Pizza) #Good
print(a_pizza) #can‘t call this
print(a_pizza.size)
print(f"Price: ${a_pizza.price()}") #Method call

another_pizza: Pizza = Pizza("small",0) #Constructor Call
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}") #Method Call
