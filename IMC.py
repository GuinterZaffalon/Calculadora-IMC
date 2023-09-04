# Calculadora de IMC em Python!

usuario = input("Seja bem-vindo! Gostaria de calcular seu IMC conosco? (sim/não) ")

if usuario == 'sim':
    peso = float(input("Qual seu peso em quilogramas? "))
    altura = float(input("Qual sua altura em metros? "))

    imc = peso / (altura ** 2)

    print("Seu IMC é:", imc)

    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif 18.5 <= imc < 24.9:
        print("Seu peso está normal.")
    elif 25 <= imc < 29.9:
        print("Você está com sobrepeso.")
    else:
        print("Você está obeso.")
elif usuario == 'não':
    print("Obrigado, estou à disposição.")
else:
    print("Opção inválida. Por favor, responda com 'sim' ou 'não'.")
