print ("Programa que calcula o preço de alugel de um carro baseado em dias/kms rodados")

dias = float (input("Quantos dias?: "))
kmrodados = float (input("Quantos km rodados?: "))
precodias = 100*dias
precokms = 5*kmrodados
precofinal = precodias+precokms

print (f"O preço do carro foi {precofinal:.2f}")
