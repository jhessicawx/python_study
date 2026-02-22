from random import choice
aluno1 = str(input("Diga o nome do primeiro aluno: "))
aluno2 = str(input("Diga o nome do segundo aluno: "))
aluno3 = str(input("Diga o nome do terceiro aluno: "))
aluno4 = str(input("Diga o nome do quarto aluno: "))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
