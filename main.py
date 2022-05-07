from time import sleep
from win32 import win32print, win32api
import os




lista_impressoras = win32print.EnumPrinters(2)
for impressora in lista_impressoras:
    print(impressora)


principal_imp = lista_impressoras[6]
print(principal_imp[2])
win32print.SetDefaultPrinter(principal_imp[2])


a = int(input("Coloque a quantidade de cópias"))
caminho = input("Cole o caminho(imprime tudo no diretório)")
caminho = caminho


lista_arq = os.listdir(caminho)

b = 1
while b <= a:
    for arq in lista_arq:
        win32api.ShellExecute(0, "print", arq, None, caminho, 0)
        sleep(120)
        print(a)
    b += 1
    
