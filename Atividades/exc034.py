print ("Programa que calcula aumento(se ganhar 1250+ é 10%.Se for menos que isso é 15%)")
salario = int(input("Digite o seu salario: "))
aumento10 = salario*10/100
aumento15 = salario*15/100
novosalario10 = salario+aumento10
novosalario15 = salario+aumento15

if salario >= 1250:
    print (f"Com seus 10% de aumento você foi de {salario} para {novosalario10}")
else:
    print (f"Com seus 15% de aumento você foi de {salario} para {novosalario15}")