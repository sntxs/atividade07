def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    peso = float(input("Digite o seu peso (em kg): "))
    altura = float(input("Digite a sua altura (em metros): "))
    imc = calcular_imc(peso, altura)
    print("Seu IMC é:", imc)

if __name__ == "__main__":
    main()
