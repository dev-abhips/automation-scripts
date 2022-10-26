import typer

from tasks.task import TaskEntry, task_factory
from utils.functions import convert_string_to_sentence


def get_menu() -> dict:
    print("\n------------ Menu ------------\n")
    menu: dict = {}
    for name, entry in TaskEntry.__members__.items():
        print(f"{entry.value}) {convert_string_to_sentence(name, '_')}.")
        menu.update({entry.value: name})
    print("\n")
    return menu


def main() -> None:
    menu: dict = get_menu()
    choice: int = int(input("Enter the choice of action: "))
    print("\n------------------------------")
    print(f"\nYou have chosen the task `{convert_string_to_sentence(menu.get(choice), '_')}`.")
    task = task_factory(choice)
    task.run()
    print("\n------------------------------\n")


if __name__ == "__main__":
    typer.run(main)
