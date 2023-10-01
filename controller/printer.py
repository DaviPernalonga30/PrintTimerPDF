import platform


def getPrintModule():
    """
    This "Function" initilize the WindowsPrinter (In case a Win System) or the LinuxPrinter (In case a Linux System)  
    See the docs for that classes and functions.
    """
    if platform.system() == 'Windows':
        import model.windows.winprinter as winprinter
        return winprinter.WinPrinter()

    else:
        import model.linux.lprinter as linuxprinter
        return linuxprinter.LinuxPrinter()
