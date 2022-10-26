import os
from enum import Enum
from typing import List

from utils.functions import get_enum_values


class FileType(Enum):
    ALL = "all"
    CODE = "code"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"


class ImageType(Enum):
    PNG = "png"
    GIF = "gif"
    JPG = "jpg"
    JPEG = "jpeg"
    WEBP = "webp"


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
    MOV = "mov"
    SRT = "srt"  # subtitle file
    FLAC = "flac"
    THREEGP = "3gp"


class DocumentType(Enum):
    DOC = "doc"
    DOCX = "docx"
    XLS = "xls"
    XLSX = "xlsx"
    PPT = "ppt"
    PPTX = "pptx"
    OTP = "otp"
    OTT = "ott"
    ODS = "ods"
    ODT = "odt"
    OPT = "opt"
    OST = "ost"
    TXT = "txt"
    OXT = "oxt"
    MD = "md"
    CSV = "csv"
    PDF = "pdf"
    MOBI = "mobi"
    EPUB = "epub"


class CodeType(Enum):
    ISO = "iso"
    DMG = "dmg"
    XML = "xml"
    JSON = "json"


def get_file_types(file_type: FileType):
    mapping = {
        FileType.CODE: get_enum_values(CodeType),
        FileType.IMAGE: get_enum_values(ImageType),
        FileType.AUDIO: get_enum_values(AudioType),
        FileType.VIDEO: get_enum_values(VideoType),
        FileType.DOCUMENT: get_enum_values(DocumentType),
    }
    return mapping.get(file_type)


class FileUtils:
    def copy_files_to_destination(self, from_dir: str, to_dir: str, file_type: FileType) -> bool:
        if not self.is_path_existing(from_dir):
            print(f"Couldn't find the directory `{from_dir}`!")
            return False
        self.create_directory_if_not_existing(to_dir)
        if not isinstance(file_type, FileType):
            print(f"Wrong file_type {str(file_type)}")
            return False

        file_types = get_file_types(file_type)
        print(f"\nCopying the {file_type.name} files from `{from_dir}` to `{to_dir}`\n")
        for file_name in os.listdir(from_dir):
            old_f = os.path.join(from_dir, file_name)
            new_f = os.path.join(to_dir, file_name)
            if os.path.isfile(old_f) and self.check_file_type(file_name, file_types):
                os.rename(old_f, new_f)
                print(f"  - {old_f} --> {new_f}")

    def check_file_type(self, file_name: str, file_types: List) -> bool:
        for file_type in file_types:
            if file_name.lower().endswith(file_type):
                return True
        return False

    def is_path_existing(self, path: str) -> bool:
        return os.path.exists(path)

    def create_directory_if_not_existing(self, path: str) -> bool:
        if os.path.isfile(path):
            print(f"`{path}` is not a directory but an existing file!!")
            return False
        if not os.path.isdir(path):
            print(f"\nCreated the directory `{path}`.")
            os.makedirs(path)
            return True
        return False
