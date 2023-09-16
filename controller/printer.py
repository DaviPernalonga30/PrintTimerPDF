import platform


def getPrintModule():
    if platform.system() == 'Windows':
        import model.windows.winprinter as winprinter
        return winprinter.WinPrinter()

    else:
        import model.linux.lprinter as linuxprinter
        return linuxprinter.LinuxPrinter()
