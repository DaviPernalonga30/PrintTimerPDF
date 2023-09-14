import cups


class LinuxPrintJob():
    def __init__(self, printer, file_path, options=None):
        self.printer = printer
        self.file_path = file_path
        self.options = options
        self.__conn = cups.Connection()

        if self.options == None:
            self.options = self.__conn.getDefaultOptions(self.printer)

    def _getJobInfo(self, index):
        pass

    def _getAllPrintJobs(self):
        pass

    def printFile(self):
        # Separa o CreatePrintJob de uma print normal
        pass

    def createPrintJob(self):
        # in this function self.file_path is the name of the print job
        # and is also the path for the file that will be printed.
        job_id = self.__conn.createJob(
            self.printer, self.file_path, self.options)

        with open(self.file_path, "rb") as file:
            self.__conn.printFile(self.printer, job_id,
                                  self.file_path, self.file_path, {})
        pass
