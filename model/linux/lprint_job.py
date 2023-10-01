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
        """
        Print specified file, the file is defined in the Class define.
        """
        self._printFile()

    def setSublimaticDefaults(self):
        """
        LINUX ONLY
        Set printer configuration to Mirrored and the Quality for the Max
        This is a simple de
        """
        self.options = {'Mirror': 'True',
                        'Print Quality': 'PLAIN_HIGH',
                        }

    def setNormalDefaults(self):
        """
        LINUX ONLY
        Set printer configuration to not Mirrored and the Quality for the normal
        This is a simple default
        """
        self.options = {'Mirror': 'False',
                        'Print Quality': 'PLAIN_NORMAL',
                        }
