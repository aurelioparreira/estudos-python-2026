def obter_dados():
      valores = []

    print("Digite 5 valores:")

    for i in range(5):
        valor = float(input(f"Valor {i+1}: "))
        valores.append(valor)

    return valores


def calcular_media(lista):
    return sum(lista) / len(lista)


def obter_maior(lista):
    return max(lista)


def obter_menor(lista):
    return min(lista)


def main():
    print("=== ANALISE DE DADOS ===")

    dados = obter_dados()

    media = calcular_media(dados)
    maior = obter_maior(dados)
    menor = obter_menor(dados)

    print("\nResultados:")
    print("Dados:", dados)
    print("Média:", media)
    print("Maior valor:", maior)
    print("Menor valor:", menor)


if __name__ == "__main__":
    main()
