print ("Acerte a senha!(4 DIGITOS)")
senha = "8226"
for i in range (1, 4):
    tentativa = input("Tente acertar a senha!")
    if tentativa == senha:
        print("Você acertou!")
        print("=====FIM DO PROGRAMA=====")
        exit()
    elif tentativa == "1234":
        print ("Obvio que não seria isso KKKKK")
    else:
        print("Você não conseguiu advinhar!")
print ("=====FIM DO PROGRAMA=====")