

class IFile:
    origin_url = ''
    thumbnail_url = ''


class IFolder:
    name = ''


class AbstractStorage:
    def list_dir(self, folder_id: str):
        raise NotImplementedError

    def save_file(self, folder_id: str, file_name: str, content: bytearray):
        raise NotImplementedError

    def move_file(self, file_id: str, destination: str):
        raise NotImplementedError

    def delete_file(self, file_id: str):
        raise NotImplementedError

    def create_folder(self, folder_name):
        raise NotImplementedError

    def move_folder(self, folder_id: str, destination: str):
        raise NotImplementedError

    def delete_folder(self, folder_id: str):
        raise NotImplementedError
