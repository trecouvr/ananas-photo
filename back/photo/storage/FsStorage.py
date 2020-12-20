from os
from .base import AbstractStorage


class FsStorage(AbstractStorage):
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def list_dir(self, folder_id: str):
        pass

    def save_file(self, folder_id: str, file_name: str, content: bytearray):
        pass

    def move_file(self, file_id: str, destination: str):
        pass

    def delete_file(self, file_id: str):
        pass

    def create_folder(self, folder_name):
        pass

    def move_folder(self, folder_id: str, destination: str):
        pass

    def delete_folder(self, folder_id: str):
        pass
