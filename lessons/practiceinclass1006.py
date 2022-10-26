"""Pracice of dictionaries."""


def zip(a: list[str], b: list[str]) -> dict[str, str]:
    """Use the first list as keys and the second list as values."""
    assert len(a) == len(b)
    zipped: dict[str, str] = {}
    for i in range (0,len(a)):
        zipped[a(i)] = b[i]
