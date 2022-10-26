"""EX05 - list utility test."""

__author__ = "730480069"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Test function only_evens when the list is empty."""
    assert only_evens([]) == []


def test_only_evens_single_item() -> None:
    """Test function only_evens when the list only contains one item."""
    xs: list[int] = [2]
    assert only_evens(xs) == [2]


def test_only_evens_many_items() -> None:
    """Test function only_evens when the list contains many items."""
    xs: list[int] = [1, 5, 3]
    assert only_evens(xs) == []


def test_concat_empty() -> None:
    """Test function concat when the two lists are both empty."""
    assert concat([], []) == []


def test_concat_single_item() -> None:
    """Test function concat when the two lists both contain one item."""
    first_list: list[int] = [1]
    second_list: list[int] = [2]
    assert concat(first_list, second_list) == [1, 2]


def test_concat_many_items() -> None:
    """Test function concat when the two lists both contain many items."""
    first_list: list[int] = [1, 2, 3]
    second_list: list[int] = [4, 5]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 5]


def test_sub_empty() -> None:
    """Test function sub when the length of the list is 0, and the start and end are both 0."""
    xs: list[int] = []
    start: int = 0
    end: int = 0
    assert sub(xs, start, end) == []


def test_sub_negative_start_large_end() -> None:
    """Test function sub when the list contains one item, the start is negative and the end index is greater than the length of the list."""
    xs: list[int] = [1]
    start: int = -1
    end: int = 2
    assert sub(xs, start, end) == []


def test_sub_normal() -> None:
    """Test function sub when the list contains many items and normal start and end."""
    xs: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(xs, start, end) == [20, 30]