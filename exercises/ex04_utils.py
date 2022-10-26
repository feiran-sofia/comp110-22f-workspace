

"""EX04 - list utility functions."""

__author__ = "730480069"


def all(library: list[int], n: int) -> bool:
    """Indicate whether or not all the ints in the list are the same as the given int."""
    i: int = 0
    if len(library) == 0:
        library.append(n + 1)
    while i < len(library):
        if n != library[i]:
            return False
        else:
            i += 1
    return True


def max(num: list[int]) -> int:
    """Return the largest value in the list."""
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
    """Check every element at two lists is equal."""
    if len(num1) != len(num2):
        return False
    a: int = 0
    while a < len(num1) and a < len(num2):
        if num1[a] == num2[a]:
            a += 1
        else:
            return False

    return True