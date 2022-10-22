import os
from typing import List
from enum import Enum
from utils.functions import get_enum_values


class FileType(Enum):
    ALL = "all"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"


class ImageType(Enum):
    PNG = "png"
    GIF = "gif"
    JPG = "jpg"
    JPEG = "jpeg"


class AudioType(Enum):
    AAC = "aac"
    MP3 = "mp3"
    M4A = "m4a"
    WAV = "wav"
    WMA = "wma"
    FLAC = "flac"


class VideoType(Enum):
    MP4 = "mp4"
    MKV = "mkv"
    FLAC = "flac"
    THREEGP = "3gp"


class DocumentType(Enum):
    DOC = "doc"
    DOCX = "docx"
    xls = "XLS"
    xlsx = "XLSX"
    ppt = "PPT"
    pptx = "PPTX"
    odt = "ODT"
    txt = "TXT"
    md = "MD"
    csv = "CSV"
    pdf = "pdf"



class FileUtils:
    def copy_files_to_destination(self, from_dir: str, to_dir: str, file_type: FileType) -> bool:
        if not self.is_path_existing(from_dir):
            print(f"Couldn't find the directory `{from_dir}`!")
            return False
        if not self.is_path_existing(to_dir):
            print(f"Couldn't find the directory `{to_dir}`!")
            return False
        if not isinstance(file_type, FileType):
            print(f"Wrong file_type {str(file_type)}")
            return False

        file_types = []
        if file_type == FileType.IMAGE:
            file_types = get_enum_values(ImageType)
        elif file_type == FileType.AUDIO:
            file_types = get_enum_values(AudioType)
        elif file_type == FileType.VIDEO:
            file_types = get_enum_values(VideoType)

        print(f"\nCopying the files of the type `{file_type.name}` from `{from_dir}` to `{to_dir}`")
        for file_name in os.listdir(from_dir):
            f = os.path.join(from_dir, file_name)
            if os.path.isfile(f) and self.check_file_type(file_name, file_types):
                print(f)

    def check_file_type(self, file_name: str, file_types: List) -> bool:
        for file_type in file_types:
                if file_name.lower().endswith(file_type):
                    return True
        return False

    def is_path_existing(self, path: str) -> bool:
        return True
