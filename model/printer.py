from win32 import win32print
from threading import Thread

# Windows specific code starts with W
# Linux specific code starts with L


class WinPrinter():
    def __init__(self):
        self.printers = None
        self.defaultPrinter = None
        self._winPrinter()

    def _winPrinter(self):
        threadGetPrinters = Thread(target=self._WgetPrinters)
        threadGetDefaulPrinter = Thread(target=self._WgetDefaultPrinter)
        threadGetPrinters.start()
        threadGetDefaulPrinter.start()
        pass

    def _linuxPrinter():
        pass

    # Windows Specific code

    def _WgetPrinters(self):
        self.printers = win32print.EnumPrinters(
            win32print.PRINTER_ENUM_LOCAL, None, 1)  # See the docs

    def _WgetDefaultPrinter(self):
        self.defaultPrinter = win32print.GetDefaultPrinterW()

    def WsetDefaulPrinter(self, index):
        if index > self.printers.__len__():
            pass
        self.defaultPrinter = self.printers[index]

        # 2 is the index of the name of the printer
        win32print.SetDefaultPrinter(self.defaultPrinter[2])
