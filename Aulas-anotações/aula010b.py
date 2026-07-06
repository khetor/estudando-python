print ("Calculadora de medias 2.0")
n1 = float(input("Digite a primeira nota: "))
n2 = float (input("Digite a segunda nota: "))
media = (n1+n2)/2

if media >= 6:
    print (f"Você passou com a média {media:.2f}")
else:
    print (f"Infelizmente você foi pra recuperção com a nota {media:.2f}")