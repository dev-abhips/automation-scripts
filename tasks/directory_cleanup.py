import os
from base.task import BaseTask
from utils.file_utils import FileUtils, FileType


class DirectoryCleanupTask(BaseTask):
    def __init__(self):
        super()
        self.file_utils = FileUtils()
        self.video_dir = os.path.expanduser("~/Videos/temp")
        self.audio_dir = os.path.expanduser("~/Music/temp")
        self.picture_dir = os.path.expanduser("~/Pictures/temp")
        self.document_dir = os.path.expanduser("~/Documents/temp")


    def get_param_values(self):
        directory = input("\nGive the path from the home directory: ")
        self.from_dir = os.path.expanduser(f"~/{directory}")
        print("\n")

    def run(self):
        self.get_param_values()
        self.file_utils.copy_files_to_destination(self.from_dir, self.video_dir, FileType.VIDEO)
        self.file_utils.copy_files_to_destination(self.from_dir, self.audio_dir, FileType.AUDIO)
        self.file_utils.copy_files_to_destination(self.from_dir, self.picture_dir, FileType.IMAGE)
        self.file_utils.copy_files_to_destination(self.from_dir, self.document_dir, FileType.DOCUMENT)
