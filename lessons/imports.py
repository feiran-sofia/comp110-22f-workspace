"""Examples of importing Python."""

from lessons import helpers
#from a package folder import a module 

from lessons import helpers as hp

from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2,4))
    print(f"The answer:{helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()
else: 
    print(f"helpers.py was imported: {__name__}")
#