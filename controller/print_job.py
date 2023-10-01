import platform


def getJobModule(printer, file_path, options=None):
    """
    Start Print Jobs:
    Parameters:  
    printer -- Need to pass the printer, the best pratice is to pass by the printer module. like this: getPrintModule().defautprinter |
    file_path -- The file path is the path to the file |
    options -- The Options is linux only, but is not mandatory 

    This "Function" initilize the WindowsPrintJob (In case a Win System) or the LinuxPrintJob (In case a Linux System)  
    See the docs for that classes and functions.

    """
    if platform.system() == 'Windows':
        import model.windows.winprint_job as winjob
        return winjob.WindowsPrintJob(printer, file_path, options)

    else:
        import model.linux.lprint_job as linuxjob
        return linuxjob.LinuxPrintJob(printer, file_path, options)
