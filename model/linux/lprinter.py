import cups as cups
import threading


class LinuxPrinter():
    def __init__(self):
        self.printers = None
        self.printersName = []
        self.defaultPrinter = None
        self.__conn = cups.Connection()
        thread = threading.Thread(target=self.__printer)
        thread.start()
        thread.join()

    def __printer(self):
        self._getPrinters()
        self._getDefaultPrinter()
        self._getPrintersNameList()

    def _getPrintersNameList(self):
        for pr in self.printers:
            self.printersName.append(pr)

    def _getPrinters(self):
        self.printers = self.__conn.getPrinters()

    def _getDefaultPrinter(self):
        self.defaultPrinter = self.__conn.getDefault()

    def setDefaultPrinter(self, index):
        if index >= self.printers.__len__():
            return
        self.defaultPrinter = self.printersName[index]
        self.__conn.setDefault(self.defaultPrinter)
