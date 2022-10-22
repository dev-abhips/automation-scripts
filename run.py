from enum import Enum

import typer
from tasks.duplicate_detector_task import DuplicateDetectorTask
from tasks.downloads_cleanup import DirectoryCleanupTask


class Choice(Enum):
    MANIPULATE_DUPLICATE = 1
    CLEANUP_DIRECTORY = 2


def main() -> None:
    """
    Manage duplicates Task: Detect the duplicate files in a directory and
    notify the user.
    """
    print("\n------------ Menu ------------\n")
    print("1) Manage duplicates")
    print("2) Cleanup downloads")
    choice = int(input("Enter the choice of action: "))
    if choice == Choice.MANIPULATE_DUPLICATE.value:
        print("\nManaging duplicates.")
        task = DuplicateDetectorTask()
    elif choice == Choice.CLEANUP_DIRECTORY.value:
        print("\nCleanup Downloads.")
        task = DirectoryCleanupTask()
    task.run()
    print("\n------------------------------\n")

if __name__ == "__main__":
    typer.run(main)
