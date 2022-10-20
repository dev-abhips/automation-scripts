from enum import Enum

import typer


class Choice(Enum):
    MANIPULATE_DUPLICATE = 1


def main() -> None:
    print("\n------------ Menu ------------\n")
    print("1) Manage duplicates\n")
    choice = int(input("Enter the choice of action: "))
    if choice == Choice.MANIPULATE_DUPLICATE.value:
        print("\nManaging duplicates.")
    print("\n------------------------------\n")

if __name__ == "__main__":
    typer.run(main)
