import os


class Mime(object):

    FILE_MIMES = {
        '.css': 'text/css',
        '.html': 'text/html',
        '.jpeg': 'image/jpeg',
        '.jpg': 'image/jpg',
        '.js': 'application/javascript'
    }

    DEFAULT = 'text/plain'

    @staticmethod
    def for_ext(file_key):
        filename, file_ext = os.path.splitext(file_key)
        return Mime.FILE_MIMES.get(file_ext, Mime.DEFAULT)

