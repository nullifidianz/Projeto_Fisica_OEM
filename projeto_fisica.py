import math
c = (3*10^8)

#Bm = (Em/c)

#calculos 2

#if y == "f":
#    lambda = (c/f)
#    k = (2*math.pi/lambda)
#    ω = (2*math.pi*f)
#if y == "lambda" or y == "λ":
#   f = (c/lambda)
#   k = (2*math.pi/lambda)
#   ω = (2*math.pi*f)
#if y == "k":
#   lambda = (c/f)
#   f = (c/lambda)
#   k = (2*math.pi/lambda)
#   ω = (2*math.pi*f)
#if y == "ω" or y == "Frequência Angular":
#   f = (ω/(2*math.pi))
#   k = (2*math.pi/lambda)
#   lambda = (c/f) 
    


def info():
    print("Programa para o estudo das ondas eletromagnéticas")
    print("Este programa procura realziar conversões entre diferentes unidades e calcular valores como:\n*frequência\n*comprimento de onda\n*número de onda\n*frequência angular\n*amplitude do campo elétrico\n*amplitude do campo magnético\n*intensidade")
    print()
    print("Feito por: João Paulo Paggi Zuanon Dias - RA: 22.222.058-4")
    print("Feito por: Matheus - RA: xx.xxx.xxx-x")
    print("Feito por: Leandro - RA: xx.xxx.xxx-x")
    print()
    print("***************************************************************",)

def menu():
    print("Escolha uma opção:")
    print("\t1. Calcular valores a partir de Em, Bm ou I")
    print("\t2. Calcular valores a partir de f, λ (lambda), k ou ω")
    print("\t3. Sair")

def calculos1():
    print("Calculos a partir de Em, Bm e I")
    x = input("Escolha a grandeza Em / Bm / I: ")

    if x=="Em":
        Em = float(input("informe a amplitude do Campo Elétrico (Em) em V/m: "))
        Bm = (Em/c)
        I = (0.5*Em*Bm)
        print(f"A amplitude do Campo Magnético (Bm): {Bm:.3e} T")
        print(f"Intensidade (I): {I:.3e} W/m^2")
    elif x=="Bm":
        Bm = float(input("Informe a amplitude do Campo Magnético (Bm) em V/m: "))
        Em = (Bm*c)
        I = (0.5*Em*Bm)
        print(f"A amplitude do Campo Elétrico (Em): {Em:.3e} T")
        print(f"Intensidade (I): {I:.3e} W/m^2")
    elif x=="i":
        I = float(input("Informe a intensidade (I) em W/m^2: "))
        Em = math.sqrt(2*I)
        Bm = (Em/c)
        print(f"A amplitude do Campo Elétrico (Em): {Em:.3e} T")
        print(f"A amplitude do Campo Magnético (Bm): {Bm:.3e} T")
    else:
        print("Opção Inválida.")

def calculos2():
    print("Calculos a partir de f, λ (lambda), k ou ω (Frequência Angular)")
    y = input("Escolha a grandeza a partir de f, λ (lambda), k ou ω (Frequência Angular): ")

    if y=="f":
        print("Teste f")
    
    elif y=="lambda" or y=="λ":
        print("teste lambda")
    
    elif y=="k":
        print("teste k")
    
    elif y=="ω" or y=="Freqência Angular":
        print("teste Frequência Angular")
    else:
        print("Opção Inválida.")



def main():
    info()
    while True:
        menu()
        escolha = int(input("Digite a escolha desejada: "))
        if escolha == 1:
            calculos1()
        elif escolha == 2:
            calculos2()
        elif escolha == 3:
            print("Finalizando programa.")
            break
        else:
            print("escolha inválida, por favor digite novamente.")
        
if __name__ == "__main__":
    main()