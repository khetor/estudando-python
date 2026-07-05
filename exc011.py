print ("Calculador de area e de gasto de litros de tinta (2m² por litro)")
altura = float (input("Qual a altura?: "))
largura = float (input("Qual a largura?: "))
area = altura*largura
litros = area/2
print (f"A aréa é {area} m² e vamos precisar de {litros:.2f} litros de tinta")