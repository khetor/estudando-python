print ("""Programa que lê um nome completo e diz:
O nome com todas as letras maiusculas,
o nome com todas minusculas,
quantas letras ao todo(sem espaço,)
quantas letras so o primeiro nome.""")
nome = input("Digite o nome: ")
print (nome.upper())
print (nome.lower())
print (len(nome.replace (" ","")))
nomesplit = nome.split(" ")
print (len(nomesplit[0]))