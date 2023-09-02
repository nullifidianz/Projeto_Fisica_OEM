import math
c = 3*10**8

def info():
    print("Programa para o estudo das ondas eletromagnéticas proposto pela matéria CF3121 - Tópicos de Optica e Física Moderna")
    print()
    print("Este programa procura realizar conversões entre diferentes unidades e calcular valores como:\n*frequência\n*comprimento de onda\n*número de onda\n*frequência angular\n*amplitude do campo elétrico\n*amplitude do campo magnético\n*intensidade")
    print()
    print("Feito por: João Paulo Paggi Zuanon Dias - RA: 22.222.058-4")
    print("Feito por: Mateus Rocha - RA: 22.222.022-2")
    print("Feito por: Leandro de Brito Alencar - RA: 22.222.034-5")
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
        Bm = float(input("Informe a amplitude do Campo Magnético (Bm) em T: "))
        Em = (Bm*c)
        I = (0.5*Em*Bm)
        print(f"A amplitude do Campo Elétrico (Em): {Em:.3e} V/m")
        print(f"Intensidade (I): {I:.3e} W/m^2")
    elif x=="i":
        I = float(input("Informe a intensidade (I) em W/m^2: "))
        Em = math.sqrt(2*I)
        Bm = (Em/c)
        print(f"A amplitude do Campo Elétrico (Em): {Em:.3e} V/m")
        print(f"A amplitude do Campo Magnético (Bm): {Bm:.3e} T")
    else:
        print("Opção Inválida.")

def calculos2():
    print("Calculos a partir de f, λ (lambda), k ou ω (Frequência Angular)")
    y = input("Escolha a grandeza a partir de f, λ (lambda), k ou ω (Frequência Angular): ")

    if y=="f":
        f = float(input("Informe a frequência (f): "))
        lamb = (c/f)
        k = (2*math.pi/lamb)
        ω = (2*math.pi*f)
        print(f"Comprimento de onda (λ): {lamb:.3e} m")
        print(f"Número de onda (k): {k:.3e} rad/m")
        print(f"Frequência angular (ω): {ω:.3e} rad/s") 
    elif y=="lambda" or y=="λ":
        lamb = float(input("Informe o comprimento de Onda (λ) em metros: "))
        f = (c/lamb)
        k = (2*math.pi/lamb)
        ω = (2*math.pi*f)
        print(f"Frequência (f): {f:.3e} Hz")
        print(f"Número de onda (k): {k:.3e} rad/m")
        print(f"Frequência angular (ω): {ω:.3e} rad/s")
    elif y=="k":
        k = float(input("Informe o número de onda (k) em rad/m: "))
        lamb = (2*math.pi/k )  
        f = (c/lamb)     
        ω = (c*k)   
        print(f"Frequência (f): {f:.3e} Hz")
        print(f"Comprimento de onda (λ): {lamb:.3e} m")
        print(f"Frequência angular (ω): {ω:.3e} rad/s")
    
    elif y=="ω" or y=="Frequência Angular":
        ω = float(input("Informe a frequência angular (ω) em rad/s: "))
        f = (ω/(2*math.pi))  
        lamb = (c/f)    
        k = (2*math.pi/lamb)     
        print(f"Frequência (f): {f:.3e} Hz")
        print(f"Comprimento de onda (λ): {lamb:.3e} m")
        print(f"Número de onda (k): {k:.3e} rad/m")
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
