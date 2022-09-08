

"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730480069"

secret: str = input("Enter a 5-character word:")
secret_length: int = len(secret)
if secret_length != 5:
    print("Error: Word must contain 5 characters")
    exit()

guess: str = (input("Enter a single character:"))
guess_length: int = len(guess)
if guess_length != 1:
    print("Error: Character must be a single character.")
    exit()

character1: str = secret[0]
character2: str = secret[1]
character3: str = secret[2]
character4: str = secret[3]
character5: str = secret[4]
times: int = int(secret.count(guess))

print("searching for " + guess + " in " + secret)

if guess == character1:
    print(guess + " found at index 0")
if guess == character2:
    print(guess + " found at index 1")
if guess == character3:
    print(guess + " found at index 2")
if guess == character4:
    print(guess + " found at index 3")
if guess == character5:
    print(guess + " found at index 4")

if times == 1:
    print(times, "instance of " + guess + " found in " + secret)
else:
    if times == 0:
        print("No instances of " + guess + " found in " + secret)
    else:
        print(times, "instances of " + guess + " found in " + secret)