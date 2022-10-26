"""EX05 - more list utility."""

__author__ = "730480069"


def only_evens(xs: list[int]) -> list[int]:
    """Find even numbers in a list."""
    i: int = 0
    result: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            result.append(xs[i])
        i += 1
    return result


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Combine two lists."""
    a: int = 0
    combined_list: list[int] = []
    while a < len(first_list):
        combined_list.append(first_list[a])
        a += 1
    a = 0
    while a < len(second_list):
        combined_list.append(second_list[a])
        a += 1
    return combined_list


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Create a sublist for a list."""
    sublist: list[int] = []
    if start < 0:
        start = 0
    if end > len(xs):
        end = len(xs)
    if len(xs) == 0 or start > len(xs) or end <= 0:
        return sublist
    while start <= (end - 1):
        sublist.append(xs[start])
        start += 1
    return sublist
