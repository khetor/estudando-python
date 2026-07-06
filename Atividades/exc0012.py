print ("Programa que lê o preço de um produto e mostra ele com 5% de desconto.")
produto = float(input("Digite o valor do produto R$: "))
desconto = produto*5/100
precofinal = produto-desconto
print (f"O produto era R${produto} e agora custa R${precofinal}")