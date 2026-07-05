print ("Programa de conversão de medidas(em metros)")

metrosbase = float (input("Digite o valor que será convertido: "))
print (f"A medida de {metrosbase} metros equiivale a:")

print (metrosbase/1000,"km")
print (metrosbase/100,"hm")
print (metrosbase/10,"dam")
print (metrosbase*10,"dm")
print (metrosbase*100,"cm")
print (metrosbase*1000,"mm")
