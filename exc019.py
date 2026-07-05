print ("Programa que sorteia um aluno para apagar a lousa")
import random
aluno1 = (input("Escreva o nome do primeiro aluno: "))
aluno2 = (input("Escreva o nome do segundo aluno: "))
aluno3 = (input("Escreva o nome do terceiro aluno: "))
aluno4 = (input("Escreva o nome do quarto aluno: "))
alunos = [aluno1,aluno2,aluno3,aluno4]
print (f"O aluno escolhido para apagar a lousa foi {random.choice(alunos)}")
