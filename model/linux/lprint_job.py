import cups


class LinuxPrintJob():
    def __init__(self, printer, file_path, options=None):
        self.printer = printer
        self.file_path = file_path
        self.options = options
        self.__conn = cups.Connection()
        if self.options == None:
            self.options = {}  # self.__conn.getPrinterAttributes(self.printer)

    def _printFile(self):
        job_name = self.file_path
        self.__conn.printFile(self.printer, self.file_path,
                              job_name, self.options)

    def startJob(self):
        self._printFile()

    def setSublimaticDefaults(self):
        self.options = {'Mirror': 'True',
                        'Print Quality': 'PLAIN_HIGH',
                        }

    def setNormalDefaults(self):
        self.options = {'Mirror': 'False',
                        'Print Quality': 'PLAIN_NORMAL',
                        }
