# Create a fixed path or personilized path
import os


class DefaultPath():
    def __init__(self):
        self.home = os.path.expanduser('~')
        self.homeJobFolder = None
        self.plataform = None

    def _windownsJobFolder():
        pass

    def _linuxJobFolder():
        pass

    def _getPlataform():
        pass
