import platform


def getJobModule(printer, file_path, options=None):
    if platform.system() == 'Windows':
        import controller.winprint_job as winjob
        return winjob

    else:
        import controller.lprint_job as linuxjob
        return linuxjob.LinuxPrintJob(printer, file_path, options)
