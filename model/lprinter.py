import cups as cups
import threading


class LinuxPrinter():
    def __init__(self):
        self.printers = None
        self.defaultPrinter = None
        self.__conn = cups.Connection()
        thread = threading.Thread(target=self.__printer)
        thread.start()
        thread.join()

    def __getPrintersNameList(self):
        aux = []
        for pr in self.printers:
            aux.append(pr)
        return aux

    def __printer(self):
        self._getPrinters()
        self._getDefaultPrinter()

    def _getPrinters(self):
        self.printers = self.__conn.getPrinters()

        pass

    def _getDefaultPrinter(self):
        self.defaultPrinter = self.__conn.getDefault()
        pass

    def setDefaultPrinter(self, index):
        if index >= self.printers.__len__():
            return
        aux = self.__getPrintersNameList()
        print(aux)
        self.defaultPrinter = aux[index]
        self.__conn.setDefault(self.defaultPrinter)
