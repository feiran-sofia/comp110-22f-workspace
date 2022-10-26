"""Test of the utilities of dictionary."""

__author__ = "730480069"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Test function invert when the dictionary is empty."""
    assert invert({}) == {}


def test_invert_one_pair() -> None:
    """Test function invert when the dictionary has one pair."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert_key_two_pairs() -> None:
    """Test function invert when the dictionary has two pairs."""
    assert invert({'apple': 'cat', 'banana': 'dog'}) == {'cat': 'apple', 'dog': 'banana'}


def test_favorite_color_empty() -> None:
    """Test function favorite color when the dictionary is empty."""
    assert favorite_color({}) == ""


def test_favorite_color_one_most() -> None:
    """Test function favorite color when the dictionary has one color that has the highest frequency."""
    assert favorite_color({'kris': 'yellow', 'michael': 'blue', 'marc': 'blue'}) == "blue"


def test_favorite_color_two_most() -> None:
    """Test function favorite color when the dictionary has two colors that have the highest frequency."""
    assert favorite_color({'kris': 'yellow', 'michael': 'blue', 'marc': 'blue', 'ezri': 'yellow'}) == "yellow"


def test_count_empty() -> None:
    """Test function count when the dictionary is empty."""
    assert count([]) == {}


def test_count_two_words() -> None:
    """Test function count when the dictionary has two words."""
    assert count(['apple', 'banana', 'banana']) == {'apple': 1, 'banana': 2}


def test_count_three_words() -> None:
    """Test function count when the dictionary has two words."""
    assert count(['apple', 'banana', 'banana', "berry"]) == {'apple': 1, 'banana': 2, 'berry': 1}