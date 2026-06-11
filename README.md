Todos os codigos estão com os enunciados no comentario, portando pode se consultar por aqui tambem!!
_______________________________________________________________________________________________________________________________________
Treinando variáveis

1. Boas-vindas Personalizadas: Crie uma variável para armazenar o nome de
uma pessoa. Peça para o usuário digitar seu nome, armazene-o e depois exiba a
mensagem: "Olá [nome], seja bem-vindo!".

2. Endereço Completo: Crie três variáveis: cidade, estado e cep. Peça ao
usuário para preencher cada uma e, ao final, exiba o endereço formatado em
uma única linha.

3. Soma de Dois Números: Receba dois números inteiros do usuário, armazeneos em variáveis distintas, calcule a soma e exiba o resultado.
   
4. Calculadora de Idade: Crie uma variável para o ano_nascimento e outra para
o ano_atual. Peça os dados ao usuário, subtraia as variáveis e exiba: "Sua
idade é ou será [resultado] anos".

5. Desafio Calculadora de Gorjeta: * Receba o valor total da conta de um
restaurante. Receba a porcentagem de gorjeta que o cliente deseja deixar (ex:
10, 15 ou 20).
Calcule o valor da gorjeta e o valor total final (conta + gorjeta).
Exiba os dois valores separadamente.
_______________________________________________________________________________________________________________________________________
Treinando Python

Exercício 1 – Cadastro interativo
Crie um programa que:
• Pergunte o nome do aluno
• Pergunte a idade
• Pergunte se está matriculado (True ou False)
• Mostre tudo organizado na tela

Exercício 2 – Ano de nascimento
O programa deve:
• Perguntar o nome
• Perguntar o ano de nascimento
• Usar o ano atual como constante
• Calcular e mostrar a idade

Exercício 3 – Calculadora com input
Peça dois números ao usuário e mostre:
• Soma
• Subtração
• Multiplicação
• Divisão

Exercício 4 – Número Par
Peça um número inteiro e verifique se ele é:
• Par

Exercício 5 – Divisão inteira explicada
Peça dois números e mostre:
• Divisão inteira
• Resto da divisão
• Explique com comentários no código.

Exercício 6 – Maior de idade
Nessa exercício pergunte a idade e mostre se a pessoa é maior de
idade.

Exercício 7 – Média do aluno
Peça:
• Duas notas
• Calcule a média e diga se o aluno está aprovado (média ≥ 7).

Exercício 8 – Acesso ao sistema
Pergunte ao usuário:
• Se está logado
• Se é administrador
• Verifique se ele pode acessar o sistema.

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
_______________________________________________________________________________________________________________________________________
Atividades funções python

1. Crie um programa que tenha uma função que:
Receba dois números
Retorne o maior deles.

2. Crie um programa, cuja função:
Receba um valor em Reais
Retorne o valor com 15% de imposto.

3. Crie um programa que tenha:
Uma função para calcular o IMC
Uma função para classificar o IMC
Usar as duas funções e retornar ao usuário tanto o valor de IMC e a
categoria.
_______________________________________________________________________________________________________________________________________
Treino em Python

Contar números pares até N
• Escreva um programa que receba um número N e conte quantos números pares existem
de 1 até N

Senha com tentativas
• Escreva um programa que solicite uma senha e permita até 3 tentativas. Se acertar, exiba
“Acesso permitido”, senão “Bloqueado”.

Somatório até zero
• Escreva um programa que leia números até o usuário digitar 0. Ao final, exiba a soma dos
números digitados.
• Exemplo: usuário digita 3 = operação 3+0(sendo zero o total anterior)
usuário digita 5 = operação 5 + 3(sendo 3 o valor do total anterior)
• Usuário digita 7 = operação 7 + 8(sendo 8 o valor do total anterior)

Menu interativo
• Crie um menu com opções:
o 1 → Somar dois números
o 2 → Tabuada
o 0 → Sair
• Use while para repetir até escolher sair.
o O programa deve ao ser selecionada a opção 1, solicitar que o usuário digite os
valores e retornar o total da soma
o O programa deve quando informado a opção 2, solicitar o número para a
tabuada e retornar para o usuário a tabuada correspondente ao número
informado:
5 X 1 = 5
5 x 2 = 10
5 x 3 = 15
o Ao finalizar o programa exibir uma mensagem ao usuário:
“Obrigada por utilizar o app EDN cálculos, se precisar de um novo cálculo volte a
nos procurar.”

Crie um programa que:
• Permita cadastrar alunos com nome e idade.
• Armazene os dados em uma lista.
• Exiba um menu com opções:
o 1 → Cadastrar aluno
o 2 → Listar alunos cadastrados
o 0 → Sair
• Use variáveis, if/else e laços de repetição para controlar o fluxo.
_______________________________________________________________________________________________________________________________________
O Conversor de Temperatura do Data Center

Foco: Entender a passagem de parâmetros e o retorno simples de valores
(return).

📝 Enunciado:
Os servidores de um Data Center possuem sensores automáticos que medem a
temperatura interna em graus Fahrenheit (°F). No entanto, a equipe de monitoramento do
Brasil precisa ler esses dados em graus Celsius (°C).
Crie um programa em Python que tenha uma função chamada converter_para_celsius.
Essa função deve receber a temperatura em Fahrenheit como parâmetro, calcular a
conversão e retornar o valor em Celsius. No programa principal, solicite a temperatura ao
usuário, chame a função e exiba o resultado formatado com duas casas decimais.
● Fórmula de conversão: C = (F - 32) x 5/9

📝 Enunciado:
Uma empresa de suporte técnico N1 atende três tipos de demandas de clientes: "sistema",
"rede" ou "hardware". O tempo limite de atendimento (SLA) muda de acordo com o setor
afetado.
Crie um programa que tenha uma função chamada verificar_sla. Ela deve receber o nome
do setor afetado, tratar o texto para evitar erros de digitação e retornar a string com o
tempo padrão de atendimento. Se o setor digitado for inválido, deve retornar "Setor
desconhecido".
● Regras de Negócio:
○ Se for "sistema" -> Retornar "SLA: 4 horas (Prioridade Média)"
○ Se for "rede" -> Retornar "SLA: 2 horas (Prioridade Alta)"
○ Se for "hardware" -> Retornar "SLA: 24 horas (Prioridade Baixa)"

📝 Enunciado:
Para monitorar a qualidade do link de internet de uma filial, o sistema de suporte realizou 4
testes automáticos de resposta de rede (Ping), medidos em milissegundos (ms).
Crie um programa com duas funções que trabalhem juntas:
1. A primeira função deve se chamar calcular_media_ping. Ela recebe a lista de testes,
soma todos os valores, divide pela quantidade de testes e retorna a média
aritmética calculada.
2. A segunda função deve se chamar avaliar_conexão. Ela recebe o número da média
calculado pela primeira função. Se a média for menor ou igual a 50ms, ela retorna
a mensagem "Conexão Estável". Caso contrário, retorna "Aviso: Conexão instável
ou sob alta carga".
