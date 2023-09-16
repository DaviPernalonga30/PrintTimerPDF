import cups


class LinuxPrintJob():
    def __init__(self, printer, file_path, options=None):
        self.printer = printer
        self.file_path = file_path
        self.options = options
        self.__conn = cups.Connection()
        if self.options == None:
            self.options = {}  # self.__conn.getPrinterAttributes(self.printer)

    def _getJobInfo(self, job_id):
        raw_info = self.__conn.getJobAttributes(job_id)
        # Tratar dados:
        info = raw_info
        return info

    def _getAllJobs(self):
        return self.__conn.getJobs(self.printer, myJobs=True)

    def _printFile(self):
        job_name = self.file_path
        self.__conn.printFile(self.printer, self.file_path,
                              job_name, self.options)

    def startJob(self):
        self._printFile()
