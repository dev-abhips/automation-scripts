from enum import Enum

import typer
from tasks.duplicate_detector_task import DuplicateDetectorTask
from tasks.directory_cleanup import DirectoryCleanupTask
from utils.functions import convert_string_to_sentence


class Choice(Enum):
    MANIPULATE_DUPLICATE = 1
    CLEANUP_DIRECTORY = 2

    def get_menu():
        print("\n------------ Menu ------------\n")
        menu: dict = {}
        for name, entry in Choice.__members__.items():
            print(f"{entry.value}) {convert_string_to_sentence(name, '_')}.")
            menu.update({entry.value: name})
        print("\n")
        return menu


def main() -> None:
    choices: dict = Choice.get_menu()
    choice: int = int(input("Enter the choice of action: "))
    print(f"\nYou have chosen the task `{convert_string_to_sentence(choices.get(choice)), '_'}`.")
    if choice == Choice.MANIPULATE_DUPLICATE.value:
        task = DuplicateDetectorTask()
    elif choice == Choice.CLEANUP_DIRECTORY.value:
        task = DirectoryCleanupTask()
    task.run()
    print("\n------------------------------\n")


if __name__ == "__main__":
    typer.run(main)
