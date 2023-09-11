from win32 import win32api
from model.printer import Printer


class PrintingShell():
    def print(self, arq, path):
        win32api.ShellExecute(0, "print", arq, None, path, 0)
