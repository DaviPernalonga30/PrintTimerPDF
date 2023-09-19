import platform


def getJobModule(printer, file_path, options=None):
    if platform.system() == 'Windows':
        import model.windows.winprint_job as winjob
        return winjob.WindowsPrintJob(printer, file_path, options)

    else:
        import model.linux.lprint_job as linuxjob
        return linuxjob.LinuxPrintJob(printer, file_path, options)
