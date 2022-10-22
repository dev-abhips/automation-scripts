from enum import Enum

import typer
from tasks.duplicate_detector_task import DuplicateDetectorTask


class Choice(Enum):
    MANIPULATE_DUPLICATE = 1


def main() -> None:
    """
    Manage duplicates Task: Detect the duplicate files in a directory and
    notify the user.
    """
    print("\n------------ Menu ------------\n")
    print("1) Manage duplicates\n")
    choice = int(input("Enter the choice of action: "))
    if choice == Choice.MANIPULATE_DUPLICATE.value:
        print("\nManaging duplicates.")
        task = DuplicateDetectorTask()
    print("\n------------------------------\n")

if __name__ == "__main__":
    typer.run(main)
