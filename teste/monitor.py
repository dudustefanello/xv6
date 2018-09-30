import sys
import time

while True:    
    arquivo = open('teste.txt', 'r', -1)
    texto = arquivo.read()
    linhas = texto.splitlines()
    print(len(linhas))
    arquivo.close()
    time.sleep(1)
    
