from logging import FileHandler as PyFileHandler
from datetime import datetime


class FileHandler(PyFileHandler):
    def __init__(self, filename, datefmt='%Y-%m-%d', mode='a', encoding=None, delay=False, errors=None):
        filename = filename.format(date=datetime.now().strftime(datefmt))
        super(FileHandler, self).__init__(
            filename=filename,
            mode=mode,
            encoding=encoding,
            delay=delay,
            errors=errors
        )
