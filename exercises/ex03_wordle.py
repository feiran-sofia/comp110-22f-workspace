

"""EX03 - structured wordle."""

__author__ = "730480069"


def contains_char(search_word: str, search_char: str) -> bool:
    """Check if the characer searched is found at any index of the word."""
    assert len(search_char) == 1
    i: int = 0 
    while i < len(search_word): 
        if search_word[i] == search_char:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Give a string of emoji whose color codifies your guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    a: int = 0
    while a < len(secret):
        if guess[a] == secret[a]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[a]) is True:
            emoji += YELLOW_BOX
        elif contains_char(secret, guess[a]) is False:
            emoji += WHITE_BOX
        a += 1
    return (emoji)


def input_guess(lengthguess: int) -> str:
    """Give a expected length to the guess."""
    guess_str: str = input(f"Enter a {lengthguess} character word: ")
    while len(guess_str) != lengthguess:
        guess_str = input(f"That wasn't {lengthguess} chars! Try again: ")
    else:
        return (guess_str)


def main() -> None:
    """The entry point of the program and main game loop."""
    x: int = 1
    check: bool = False
    my_secret: str = "codes"
    my_guess: str = ""
    while x <= 6 and check is False:
        print(f"=== Turn {x}/6 ===")
        my_guess = input_guess(len(my_secret))
        if my_guess != my_secret:
            print(emojified(my_guess, my_secret))
            x += 1
            if x > 6:
                print("X/6 - Sorry, try again tomorrow!")
        else:
            print(emojified(my_guess, my_secret))
            print(f"You won in {x}/6 turns!")
            check = True
    


            
