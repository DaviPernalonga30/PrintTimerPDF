# https://www.youtube.com/watch?v=ii28Nn9WENQ
# http://timgolden.me.uk/python/win32_how_do_i/print.html

from win32 import win32print


class WindowsPrintJob():
    def __init__(self, printer, file_path, options=None):
        self.printer = printer
        self.file_path = file_path
        self.options = options
        if self.options == None:
            self.options = {}  # Printer defaults configuration.

        self._handler = None
        self.__getHandler()
        self._dataTuple = (self.file_path, None, "emf")

    def __getHandler(self):
        self._handler = win32print.OpenPrinter(
            printer=self.printer, Defaults=self.options)

    def _printFile(self):
        win32print.StartDocPrinter(self._handler, self._dataTuple)

    def startJob(self):
        self._printFile()
        win32print.ClosePrinter(self._handler)
