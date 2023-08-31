import math
c = (3*10^8)

#Bm=(Em/c)


def info():
    print("Programa para o estudo das ondas eletromagnéticas")
    print("Este programa procura realziar conversões entre diferentes unidades e calcular valores como:\nfrequência\ncomprimento de onda\nnúmero de onda\nfrequência angular\namplitude do campo elétrico\namplitude do campo magnético\nintensidade")
    print()
    print("Feito por: João Paulo Paggi Zuanon Dias - RA: 22.222.058-4")
    print("Feito por: Matheus - RA: xx.xxx.xxx-x")
    print("Feito por: Leandro - RA: xx.xxx.xxx-x")
    print()
    print("***************************************************************",)

def menu():
    print("Escolha uma opção:")
    print("\t1. Calcular valores a partir de Em, Bm ou I")
    print("\t2. Calcular valores a partir de f, λ, k ou ω")
    print("\t3. Sair")

def calculos1():
    print("Calculos a partir de Em, Bm e I")
    x = input("Escolha a grandeza Em / Bm / I")

    if x=="Em":
        Em = float(input("informe a amplitude do Campo Elétrico (Em) em V/m"))
        Bm = (Em/c)
        I = (0.5*Em*Bm)
        print(f"A amplitude do Campo Magnético (Bm): {Bm:.3e} T")
        print(f"Intensidade (I): {I:.3e} W/m^2")
    elif x=="Bm":
        Bm = float(input("Informe a amplitude do Campo Magnético (Bm) em V/m"))
        Em = (Bm*c)
        I = (0.5*Em*Bm)
        print(f"A amplitude do Campo Elétrico (Em): {Em:.3e} T")
        print(f"Intensidade (I): {I:.3e} W/m^2")
    elif x=="i":
        I = float(input("Informe a intensidade (I) em W/m^2"))
        Em = math.sqrt(2*I)
        Bm = (Em/c)
        print(f"A amplitude do Campo Elétrico (Em): {Em:.3e} T")
        print(f"A amplitude do Campo Magnético (Bm): {Bm:.3e} T")
    else:
        print("Opção Inválida.")


def main():
    info()
    menu()

if __name__ == "__main__":
    main()