from win32 import win32print
from threading import Thread


class WinPrinter():
    def __init__(self):
        self.printers = None
        self.defaultPrinter = None
        self.__printer()

    def __printer(self):
        threadGetPrinters = Thread(target=self._getPrinters)
        threadGetDefaulPrinter = Thread(target=self._getDefaultPrinter)
        threadGetPrinters.start()
        threadGetDefaulPrinter.start()
        pass

    # Windows Specific code

    def _getPrinters(self):
        self.printers = win32print.EnumPrinters(
            win32print.PRINTER_ENUM_LOCAL, None, 1)  # See the docs

    def _getDefaultPrinter(self):
        self.defaultPrinter = win32print.GetDefaultPrinterW()

    def setDefaultPrinter(self, index):
        if index > self.printers.__len__():
            pass
        self.defaultPrinter = self.printers[index]

        # 2 is the index of the name of the printer
        win32print.SetDefaultPrinter(self.defaultPrinter[2])
