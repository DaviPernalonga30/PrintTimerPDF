import platform


def getPrintModule():
    if platform.system() == 'Windows':
        import model.winprinter as winprinter
        return winprinter.WinPrinter()

    else:
        import model.lprinter as linuxprinter
        return linuxprinter.LinuxPrinter()
