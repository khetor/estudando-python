print ("""Programa que vê se pode aprovar um empréstimo bancario para a compra de uma casa, 
Se o valor das prestações mensais for superior a 30% do salario será negado.""")

valorcasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salario do comprador: "))
anos = int(input("Digite quantos em quantos anos o valor sera pago: "))
valorprestacao = valorcasa/(anos*12)
salario30 = salario*30/100
if valorprestacao > salario30:
   print ("Você não pode pegar esse empréstimo!")
else:
   print (f"Você pode pegar esse emprestimo! o valor da prestação é {valorprestacao:.2f}")