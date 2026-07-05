print ("Analisados de medias com eliffs(2.1)")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2
if media ==10:
    print (f"EXCELENTE! tirou{media:.2f}")
elif media >=9:
    print(f"Muito bem tirou {media:.2f}")
elif media >=8:
    print (f"Bom,tirou {media:.2f}")
elif media >=7:
    print (f"legal, {media:.2f}")
elif media >=6:
    print (f"Quase ficava de recuperação tirou {media:.2f}")
elif media>3:
    print (f"Recuperação tirou {media:.2f}")
else:
    print (f"REPROVADO! tirou {media:.2f}")