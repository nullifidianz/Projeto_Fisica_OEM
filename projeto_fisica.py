import math

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

def main():
    info()
    menu()

if __name__ == "__main__":
    main()