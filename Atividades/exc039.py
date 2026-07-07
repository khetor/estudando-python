print ("Programa de alistamento militar")
ano = int(input("Digite SOMENTE o ano que nasceu: "))
idade1menos = (input("""Você ja fez aniversário esse ano?
{DIGITE 1 PARA SIM}
{DIGITE 2 PARA NÃO}
: """))
idade = 2026-ano
if idade1menos == "2":
    idade = 2025-ano
    if idade<18:
        print ("Você ainda não pode se alistar")
        print (f"Faltam {18-idade} anos pra você se alistar!")
    elif idade == 18:
        print ("Você já esta na epoca de se alistar!")
    elif idade>18:
        print ("Você ja passou da época de se alistar!")
        print (f"Você está {18-idade} anos atrasado!")

if idade1menos == "1":
    if idade<18:
        print ("Você ainda não pode se alistar")
        print (f"Faltam {18-idade} anos pra você se alistar!")

    elif idade == 18:
        print ("Você já esta na epoca de se alistar!")
    elif idade>18:
        print ("Você ja passou da época de se alistar!")
        print (f"Você está {idade-18} anos atrasado!")