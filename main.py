from time import sleep
from win32 import win32print, win32api
import os

lista_impressoras = win32print.EnumPrinters(2)
for impressora in lista_impressoras:
    print(impressora)

principal_imp = lista_impressoras[0]
print(principal_imp[2])
win32print.SetDefaultPrinter(principal_imp[2])

a = int(input("Coloque a quantidade de cópias: "))
caminho = input("Cole o caminho(imprime tudo no diretório) ")

lista_arq = os.listdir(caminho)

b = 1
while b <= a:
    for arq in lista_arq:
        print("enviando request número: ", b)
        win32api.ShellExecute(0, "print", arq, None, caminho, 0)
        if b<a:
            sleep(240)
            print("metade do tempo, impressão: ", b)
            sleep(240)
            print("Acabou o tempo de espera, indo para a proxima impressao")
        else:
            print("Trabalho concluído")
    b += 1
