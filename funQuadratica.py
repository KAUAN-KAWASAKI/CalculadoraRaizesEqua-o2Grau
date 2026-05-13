# Calculadora de Equação Quadrática ou Equação do Segundo Grau:

import math # Importa a biblioteca matemática para usar a função de raiz quadrada

# Função para calcular as raízes de uma equação quadrática:
def calcularRaizes():
    # Solicita ao usuário os coeficientes da equação quadrática
    print("Equação Quadrática: ax² + bx + c = 0")
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))

    # Calcula o discriminante
    discriminante = b**2 - 4*a*c

    # Verifica o tipo de raízes com base no discriminante
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"As raízes são reais e diferentes: {raiz1} e {raiz2}")
    elif discriminante == 0:
        raiz = -b / (2*a)
        print(f"As raízes são reais e iguais: {raiz}")
    else:
        print("As raízes são complexas e não possuem solução real.")

# Menu principal para executar a função
while True:
    print("\n==============================================")
    print("  |     Calculadora de Equação Quadrática      |")
    print("  |  1. Calcular raízes                        |")
    print("  |  2. Sair                                   |")
    print("\n==============================================")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        calcularRaizes()
    elif escolha == '2':
        print("Encerrando a calculadora. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")