from os import system as sys

from prettier.prettierprint import prettierprint as pprint
from questions import *
from msvcrt import getch

# MAIN CODE
# INICIA O QUESTIONARIO
sys("cls") #Limpa tela
cab(-1)
getch()
sys("cls") #Limpa tela

cab(0)

for i in range(9):
    if i != 6:
        q = printQuestion(i)
        resp = input("> ").upper()
        contaPonto(i, q, letters.index(resp))
    else:
        printQ6()
    
    sys("cls") #Limpa tela
    cab(i)

#SE EMPATAR SORTEIA UMA CASA

if pontos.count(max(pontos)) > 1:
    lst = []
    for i in range(0, len(pontos)):
        if pontos[i] == max(pontos):
            lst.append(i)
    pontos[rd.randint(0,len(lst)-1)] += 3

result(pontos)

getch()