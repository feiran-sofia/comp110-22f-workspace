"""My Own Adventure."""

__author__ = "730480069"


from random import randint

BUTTERFLY: str = "\U0001F98B"
CHIPMUNK: str = "\U0001F43F"
TULIP: str = "\U0001F337"
SUNFLOWER: str = "\U0001F33B"
ROSE: str = "\U0001F339"
HIBISCUS: str = "\U0001F33A"

points: int = 0
player: str = ""
i: int = 0
b: int = 0
c: int = 0
d: int = 0


def main() -> None:
    """The program's entry point."""
    greet()
    continue_choice: str = input("do you want to continue your adventure? yes or no.")
    while continue_choice != "no":
        greet()
        continue_choice: str = input("do you want to continue your adventure? yes or no.")
    if continue_choice == "no":
        print("Looking forward to see you next time!")
    

def greet() -> None:
    """Greeting the player."""
    global player
    global points
    player = input("What is your name?")
    print(f"Hi {player}, nice to meet you! Welcome to your adventure in magic forest!")
    enterchoice: str = input(f"There is a butterfly{BUTTERFLY} and a chipmunk{CHIPMUNK} . Who do you want to follow with? Or you still have chance to type 'back' and start your adventure later.")
    if enterchoice == "butterfly":
        while points <= 4:
            num_s: str = input("Please choose a flower that you want butterfly to show you! If you guessed right, you can collect it to your bouquet. Type a number from 1-4. ")
            if num_s == "1":
                num: int = 1
            if num_s == "2":
                num: int = 2
            if num_s == "3":
                num: int = 3
            if num_s == "4":
                num: int = 4
            butterfly(num)
            num = 0
        print(f"your point is {points}!")
        points = 0
    if enterchoice == "chipmunk":
        chipmunk()
    if enterchoice == "back":
        print("Looking forward to see you next time!")


def butterfly(num: int) -> int:
    """The adventure road with butterfly."""
    global player
    global points
    global i
    global b
    global c
    global d
    if num == 1:
        choice: str = input(f"Hi {player}, do you know what flower it is {TULIP} ? You only have 3 chances for each kind.")
        if choice == "tulip":
            print("wow! you are right!")
            points += 1
            print(f"You earned one point! Now your point is {points} .")
        else:
            if i < 2:
                print("It's not quite right.")
            if i == 2:
                print("Let me tell you. It is a tulip.")
            i += 1
    if num == 2:
        choice: str = input(f"Hi{player}, do you know what flower it is {SUNFLOWER} ? You only have 3 chances for each kind.")
        if choice == "sunflower":
            print("wow! you are right!")
            points += 1
            print(f"You earned one point! Now your point is {points} .")
        else:
            if b < 2:
                print("It's not quite right.")
            if b == 2:
                print("Let me tell you. It is a sunflower.")
            b += 1
    if num == 3:
        choice: str = input(f"Hi{player}, do you know what flower it is {ROSE} ? You only have 3 chances for each kind.")
        if choice == "rose":
            print("wow! you are right!")
            points += 1
            print(f"You earned one point! Now your point is {points} .")
        else:
            if c < 2:
                print("It's not quite right.")
            if c == 2:
                print("Let me tell you. It is a rose.")
            c += 1
    if num == 4:
        choice: str = input(f"Hi{player}, do you know what flower it is {HIBISCUS} ? You only have 3 chances for each kind.")
        if choice == "hibiscus":
            print("wow! you are right!")
            print(f"You earned one point! Now your point is {points} .")
            points += 1
        else:
            if d < 2:
                print("It's not quite right.")
            if d == 2:
                print("Let me tell you. It is a hibiscus.")
            d += 1
    if i > 2 or b > 2 or c > 2 or d > 2:
        print("You have ran out of your chances to make a guess on this kind of flower. Please choose another flower.")
        return points


def chipmunk() -> None:
    """The adventure route with chipmunk."""
    global player
    global points
    life: int = 3
    a: int = 0
    print(f"Hi {player}, thank you for helping me fight with mutant chipmunks!")
    print("While you'll choose attack or defend, your army will choose too. Receiving a single attack without defense, your army will die while you will lose one life point.")
    print("However, if you attack, your army defends, nothing happens. If your army attacks, you defend, nothing happens. ")
    print("Defense costs your energy. So if you defend more than three times, you will lose a life point each time you defend.")
    print("Let's see how many chipmunks we can defeat!")
    while life > 0:
        print(f"Remain life points: {life}. Let's try!")
        action: str = input("choose: attack or defend ")
        army_act: int = randint(1, 2)
        if action == "attack":
            my_act: int = 1
            if my_act == army_act:
                life -= 1
                points += 1
                print("Congratulations! You defeated a mutant chipmunk. ")
                print("However, mutant chipbmunk attacked you. ")
            else:
                print("Your attack is defended by the mutant chipmunk. Don't give up! Let's try again!")
        if action == "defend":
            my_act: int = 2
            a += 1
            if my_act == army_act:
                print("You and mutant chipmunk both tried to defend. No one hurts.")
            if my_act != army_act:
                print("Nice! You avoided an attack from the mutant chipmunk.")
        if action != "attack" and action != "defend":
            print("Chipmunk couldn't understand your command and she left you. ")
            life = 0
        if a > 3:
            life -= 1
            print("You continue defending so you consumed one life point.")
    
    print(f"Sorry {player}, you ran out of your life points. The number of mutant chipmunks you defeated is {points}. Please try to enter the forest again. ")
    points = 0


if __name__ == "__main__":
    main()