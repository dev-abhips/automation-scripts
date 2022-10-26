from enum import Enum

from tasks.base import BaseTask
from tasks.directory_cleanup import DirectoryCleanupTask
from tasks.duplicate_detector import DuplicateDetectorTask


class TaskEntry(Enum):
    CLEANUP_DIRECTORY = 1
    MANIPULATE_DUPLICATE = 2


def task_factory(choice: int) -> BaseTask:
    assert type(choice) is int
    tasks = {
        TaskEntry.MANIPULATE_DUPLICATE.value: DuplicateDetectorTask,
        TaskEntry.CLEANUP_DIRECTORY.value: DirectoryCleanupTask
    }
    return tasks[choice]()
