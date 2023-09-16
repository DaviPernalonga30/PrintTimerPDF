from win32 import win32print
from threading import Thread


class WinPrinter():
    def __init__(self):
        self.printers = None
        self.defaultPrinter = None
        self.printersName = []
        th = Thread(target=self.__printer)
        th.start()
        th.join()

    def __printer(self):
        self._getPrinters()
        self._getDefaultPrinter()
        self._getPrintersNameList()

    def _getPrintersNameList(self):
        for pr in self.printers:
            self.printersName.append(pr[2])

    def _getPrinters(self):
        self.printers = win32print.EnumPrinters(
            win32print.PRINTER_ENUM_LOCAL, None, 1)  # See the docs

    def _getDefaultPrinter(self):
        self.defaultPrinter = win32print.GetDefaultPrinterW()

    def setDefaultPrinter(self, index):
        if index >= self.printers.__len__():
            return
        self.defaultPrinter = self.printers[index]

        # 2 is the index of the name of the printer
        win32print.SetDefaultPrinter(self.defaultPrinter[2])
