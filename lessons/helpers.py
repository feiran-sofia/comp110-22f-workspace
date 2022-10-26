"""Demonstrate defining a module imported eleswhere."""


THE_ANSWER: int = 42


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


print("helpers.py was evaluated.")

if __name__ == "__main__":
    main()
else: 
    print(f"helpers.py was imported: {__name__}")

#run the program and it will print helpers.py was imported: lessons.helpers