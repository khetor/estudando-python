print ("Programa que lê a velocidade de um carro(7 reais de multa por km excedido)")
velo = int(input("Digite a velocidade:"))
if velo > 80:
    print (f"Você ta acima da velocidade permitida e foi multado em {(velo-80)*7}")
else:
    print ("Ok pode passar dboas")