def obter_valores():
    valores = []
    
    for i in range(3):
        numero = float(input(f"Digite o valor {i+1}: "))
        valores.append(numero)
    
    return valores


def calcular_media(lista):
    return sum(lista) / len(lista)


def main():
    print("=== CALCULADORA DE MÉDIA ===")

    valores = obter_valores()
    media = calcular_media(valores)

    print("Valores digitados:", valores)
    print("Média:", media)


if __name__ == "__main__":
    main()
