print ("Programa que faz a media entre 2 notas de alunos")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2
if media < 0 or media>10:
    print ("\033[31mNota invalida!\033[m")
    exit()
if media >=7:
    print (f"Você está aprovado com média {media:.2f}")
elif media>=5:
    print (f"Você está de recuperação! (média {media:.2f})")
elif media<5:
    print (f"Você está reprovado! (média {media:.2f})")
