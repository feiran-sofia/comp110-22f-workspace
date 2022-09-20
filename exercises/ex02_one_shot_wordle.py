

"""EX02 - one shot wordle."""

__author__ = "730480069"

secret: str = "python"
guess: str = (input(f"What is your {len(secret)}-letter guess? "))
guess_length = len(guess)

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji: str = ""
same: bool = False
x: int = 0
position: int = 0

while len(guess) != len(secret):
    guess = str(input(f"That was not {len(secret)} letters! Try again: "))

if guess != secret:
    while x < len(secret):
        if guess[x] == secret[x]:
            emoji += GREEN_BOX
        else:
            while same is False and position < len(secret):
                if guess[x] == secret[position]:
                    same = True
                else:
                    position += 1
            if same is True:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
            same = False
            position = 0 
        x += 1 
    print(f"{emoji}\nNot quite. Play again soon!")
else: 
    emoji = GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX
    print(f"{emoji}\nWoo! You got it!")