"""The utilities of dictionary."""

__author__ = "730480069"


def invert(old: dict[str, str]) -> dict[str, str]:
    """Invert the order of keys and values."""
    new: dict[str, str] = {}
    for key in old:
        if old[key] in new:
            raise KeyError("The key is already in the dictionary.")
        new[old[key]] = key
    return new


def favorite_color(lib: dict[str, str]) -> str:
    """Determine the color that appears most frequently."""
    count: dict[str, int] = {}
    for item in lib:
        if lib[item] in count:
            count[lib[item]] += 1
        else:
            count[lib[item]] = 1
    x: int = 0
    most: str = ""
    for colors in count:
        if count[colors] > x:
            x = count[colors]
            most = colors
    return most
 

def count(lib: list[str]) -> dict[str, int]:
    """Count the number of times that value appeared in the input."""
    new: dict[str, int] = {}
    for item in lib:
        if item in new:
            new[item] += 1
        else:
            new[item] = 1
    return new