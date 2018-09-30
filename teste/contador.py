import re

arquivo = open('teste/teste.txt', 'r', -1)
texto = arquivo.read()
linhas = texto.splitlines()

contagem = {}

for linha in linhas:
    if not re.match('[A-Z];[0-9]{1,6}\Z', linha):
        continue

    letras = re.findall('[A-Z]', linha)
    if len(letras) > 0:
        letra = letras[0]

    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem.update({letra: 1})

for a in contagem.keys():
    print(contagem[a])
 
