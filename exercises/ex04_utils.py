

"""EX04 - list utility functions."""

__author__ = "730480069"

def all(library: list[int], n: int) -> bool:
    i: int =0
    while i < len(library):
        if n == library[i]:
            i += 1
        else:
            return False
    return True

def max(num: list[int]) -> int:
    if len(num) == 0:
        raise ValueError("max() arg is an empty List")
    current_max = num[0]
    x: int = 1
    while x < len(num):
        if num[x] > current_max:
            current_max = num[x]
        x += 1
    return current_max

def is_equal(num1: list[int], num2: list[int]) -> bool:
    a: int = 0
    b: int = 0
    while a < len(num1) and b < len(num2):
        if num1[a] == num2[b]:
            a += 1
            b += 1
        else:
            return False
    return True
