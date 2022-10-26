from enum import Enum

from .base import BaseTask
from .directory_cleanup import DirectoryCleanupTask
from .duplicate_detector import DuplicateDetectorTask


class TaskEntry(Enum):
    CLEANUP_DIRECTORY = 1
    MANIPULATE_DUPLICATE = 2


def task_factory(choice: int) -> BaseTask:
    assert isinstance(choice, int)
    tasks = {
        TaskEntry.MANIPULATE_DUPLICATE.value: DuplicateDetectorTask,
        TaskEntry.CLEANUP_DIRECTORY.value: DirectoryCleanupTask
    }
    return tasks[choice]()
