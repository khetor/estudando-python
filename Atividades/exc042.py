print ("Programa que verifica se 3 retas podem formar um triangulo:")

reta1 = int(input("Digite o comprimeto da primeira reta: "))
reta2 = int(input("Digite o comprimeto da segunda reta:"))
reta3 = int(input("Digite o comprimeto da terceira reta:"))
if (reta1+reta2>reta3) and (reta2+reta3>reta1) and (reta1+reta3>reta2):
    print ("Pode formar um triangulo!")
    if reta1==reta2==reta3:
        print ("Seu triangulo é equilatero!")
    elif reta1==reta2 or reta2==reta3 or reta1==reta3:
        print ("Seu triangulo é isosceles")
    elif reta1!=reta2 or reta2!=reta3 or reta1!=reta3:
        print ("Seu triangulo é escaleno!")
else:
    print ("Não pode formar um triangulo!")