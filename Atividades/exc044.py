print ("Programa que pede preço de um produto e mostra com juros ou descontos dependendo da forma de pagamento:")
preco = float(input("Digite o preço do produto: "))
dinheiro = preco*10/100
preconovodin = preco-dinheiro
cartaox1 = preco*5/100
precocartaox1 = preco-cartaox1
cartaox3 = preco*20/100
precocartaox3 = preco+cartaox3
print ("Digite no que você vai pagar")
print ("---A VISTA DINHEIRO---DIGITE 1")
print ("---A VISTA CARTÃO---DIGITE 2")
print ("---DUAS VEZES NO CARTÃO---DIGITE 3")
print ("---TRÊS VEZES NO CARTÃO(Ou mais)---DIGITE 4")
esc = input("-")
if esc == "1":
    print (f"\033[32mO valor a ser pago será {preconovodin}(teve 10% de desonto)\033[m")
elif esc == "2":
    print (f"\033[32mO valor a ser pago será {precocartaox1}(teve 5% de desconto)\033[m")
elif esc == "3":
    print (f"\033[33mO valor a ser pago será {preco}(Preço padrão do produto)\033[m")
elif esc == "4":
    print (f"\033[31mO valor a ser pago será {precocartaox3}(preço com 20% de juros)\033[m")
else:
    print ("\033[31mVALOR INVALIDO!\033[m")