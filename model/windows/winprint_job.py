# https://www.youtube.com/watch?v=ii28Nn9WENQ
# http://timgolden.me.uk/python/win32_how_do_i/print.html

from win32 import win32print, win32api


class WindowsPrintJob():
    def __init__(self, printer, file_path, options=None):
        self.printer = printer
        self.file_path = file_path
        self.options = options
        if self.options == None:
            self.options = {}  # Printer defaults configuration.

        self._handler = None
        self.__getHandler()
        self._dataTuple = (self.file_path, None, "raw")

    def __getHandler(self):
        self._handler = win32print.OpenPrinter(self.printer)

    def _printFile(self):
        try:
            win32print.StartDocPrinter(self._handler, self._dataTuple,  level=1)
            try:
                win32print.EndDocPrinter(self._handler)

            finally:
                win32print.ClosePrinter(self._handler)        
        except:
            win32api.ShellExecute(0, "print", self.file_path, None, self.file_path, 0)
        
    def startJob(self):
        self._printFile()
        win32print.ClosePrinter(self._handler)
