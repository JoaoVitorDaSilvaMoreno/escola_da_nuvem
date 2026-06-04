
"""
Exercício 1 – Cadastro interativo
Crie um programa que:
• Pergunte o nome do aluno
• Pergunte a idade
• Pergunte se está matriculado (True ou False)
• Mostre tudo organizado na tela
"""
print("===== Cadastro interativo: =====\n")

aluno = input("Digite o nome do Aluno: ")
idade = int(input("Digite a idade do Aluno: "))
matricula = bool(input("O aluno esta matriculado? (True -> Sim), (False -> Não): "))

if matricula:
  print(f"Aluno {aluno}, com idade de {idade} anos, com matricula ativa\n\n")
else:
  print(f"Aluno {aluno}, com idade de {idade} anos, se encontra na fila de espera\n\n")

"""
Exercício 2 – Ano de nascimento
O programa deve:
• Perguntar o nome
• Perguntar o ano de nascimento
• Usar o ano atual como constante
• Calcular e mostrar a idade
"""
print("===== Ano de nascimento: =====\n")

from datetime import date
nome = input("Digite o seu nome: ")
nascimento = int(input("Digite o ano do seu nascimento: "))
ATUAL = date.today().year

print(f"Você tem o terá {ATUAL - nascimento} anos \n\n")

"""
Exercício 3 – Calculadora com input
Peça dois números ao usuário e mostre:
• Soma
• Subtração
• Multiplicação
• Divisão
"""
print("===== Calculadora com input: =====\n")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(f"A soma entre {n1} + {n2} = {n1 + n2}")
print(f"A subtração entre {n1} - {n2} = {n1 - n2}")
print(f"A Multiplicação entre {n1} X {n2} = {n1 * n2}")
print(f"A divisão entre {n1} / {n2} = {n1 / n2} \n\n")

"""
Exercício 4 – Número Par
Peça um número inteiro e verifique se ele é:
• Par
"""
print("===== Número Par: =====\n")

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
  print(f"O número {numero} é par \n\n")
else:
  print(f"O número {numero} é impar \n\n")

"""
Exercício 5 – Divisão inteira explicada
Peça dois números e mostre:
• Divisão inteira
• Resto da divisão
• Explique com comentários no código.
"""
print("===== Divisão inteira explicada: =====\n")

#Entrada dos valores para a realização dos calculos
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

#A divisaõ inteira utiliza somente a parte inteira do número (a esquerda da virgula)
print(f"A divisão inteira entre {numero1} e {numero2} = {numero1 // numero2}")

#O resto da disão são as casas decimais apos a virgula (a direita da virgula)
print(f"O resto da divisão entre {numero1} e {numero2} = {numero1 % numero2} \n\n")

"""
Exercício 6 – Maior de idade
Nessa exercício pergunte a idade e mostre se a pessoa é maior de
idade
"""
print("===== Maior idade: =====\n")

idade = int(input("Digite a sua idade: "))

if idade >= 18:
  print(f"Você possui {idade} anos, portanto possui maior idade\n\n")
else:
  print(f"Você possui {idade} anos, portanto possui menor idade\n\n")

"""
Exercício 7 – Média do aluno
Peça:
• Duas notas
• Calcule a média e diga se o aluno está aprovado (média ≥ 7).
"""
print("===== Média d aluno: =====\n")

nota1 = float(input("Digite a primeira nota obtida: "))
nota2 = float(input("Digite a segunda nota obtida: "))
media = (nota1 + nota2) / 2

if media >= 7:
  print(f"Parabens, você atingiu o criterio minimo de média 7, portanto foi aprovado com nota {media}\n\n")
else:
  print(f"Infelismente você não atingiu o critério minimo de nota 7, portanto esta de recuperação por ter obtido nota {media}\n\n")

"""
Exercício 8 – Acesso ao sistema
Pergunte ao usuário:
• Se está logado
• Se é administrador
• Verifique se ele pode acessar o sistema.
"""
print("===== Acesso ao sistema: =====\n")

login = input("Você está logado no sistema? (sim / não): ")
admin = input("Você possui nivel administrador? (sim / não): ")

if login == "sim" or login == "Sim" or login == "SIM":
  if admin == "sim" or admin == "Sim" or admin == "SIM":
    print("Acesso concediddo com sucesso!!\n\n")
else:
  print("Acesso negado, por hierarquia de nivel ou falta de login\n\n")

"""
Exercício 9 – Desafio final
Crie um programa que:
• Pergunte:
• Nome do aluno
• Idade
• Três notas
• Calcule a média
• Verifique:
• Se é maior de idade
• Se a média é par ou ímpar
• Se está aprovado (média ≥ 7)
• Mostre tudo organizado na tela
"""
print("===== Desafio Final: =====/n")

nome_aluno = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade: "))
nota1 = float(input("Informe a primeira nota obtida: "))
nota2 = float(input("Informe a segunda nota obtida: "))
nota3 = float(input("Informe a terceira nota obtida: "))
media = (nota1 + nota2 + nota3) / 3

print("\n_______ Processando... ... ... \n")

if idade >= 18:
  print(f"O aluno(a) {nome_aluno} ja possui a maior idade")
else:
  print(f"O aluno(a) {nome_aluno} Não possui a maio idade")

if media % 2 == 0:
  print(f"A média final do aluno(a) {nome_aluno} é par")
else:
  print(f"A média final do aluno(a) {nome_aluno} é impar")

if media >= 7:
  print(f"Parabens {nome_aluno} você foi aprovado com nota {media}")
else:
  print(f"Não foi desta vez {nome_aluno}, você obteve média final de {media} e a nossa tolerancia é de 7.00, portanto esta de recuperação")