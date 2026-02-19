# Exercicio 001 - Saudacao e idade

nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))

ano_atual = 2026
idade = ano_atual - ano_nascimento

print(f"Olá, {nome}! Você tem aproximadamente {idade} anos.")
