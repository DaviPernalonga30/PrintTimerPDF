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

    def _getJobInfo(self, job_id):
        raw_info = self.__conn.getJobAttributes(job_id)
        # Tratar dados:
        info = raw_info
        return info

    def _getAllJobs(self):
        return self.__conn.getJobs(self.printer, myJobs=True)

    def _getPrinters(self):
        self.printers = self.__conn.getPrinters()

    def _getDefaultPrinter(self):
        self.defaultPrinter = self.__conn.getDefault()

    def setDefaultPrinter(self, index):
        if index >= self.printers.__len__():
            return
        self.defaultPrinter = self.printersName[index]
        self.__conn.setDefault(self.defaultPrinter)
