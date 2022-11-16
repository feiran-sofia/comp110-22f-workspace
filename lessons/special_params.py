"""Examples of optional parameters and Union types."""

from typing import Union

def hello(x: int, name: str = "World") -> str:
    #required operator should be in front of the optional parameter
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        #if name is a str
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    return greeting

def hello(name: Union[str,int] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello," + name
    return greeting

# Single-argument
print(hello("Sally"))

# no arguments!
print(hello())

#int argument works too!
print(hello(110))