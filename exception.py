class FileTypeError(Exception):
    """Неподдерживаемый формат"""
    pass

class DataError(Exception):
    """Файл поврежден"""
    pass
