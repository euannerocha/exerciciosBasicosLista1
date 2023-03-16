# Faça um Programa que mostre a mensagem "Alo mundo" na tela.
frase = "Alo Mundo"

print("A frase que estou imprimindo aqui é: {}".format(frase))

# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numeroInformado = int(input("Digite um número: "))

print("O número informado foi: {}".format(numeroInformado))

# Faça um Programa que peça dois números e imprima a soma.

numero1 = float(input("Digite número 1: "))
numero2 = float(input("Digite número 2: "))

soma = numero1 + numero2
multiplicacao = numero1 * numero2

print("A soma dos números é: {:.2f}. A multiplicação é: {:.4f}".format(soma, multiplicacao))
print(f"A soma é: {soma:.2f}, e a multiplicação é {multiplicacao:.4f}")

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if (media == 6): 
    print(f"A média final é {media:.2f}. Parabéns! Você passou, mas foi na média!")
elif(media > 6):
    print(f"A média final é {media:.2f}. Parabéns! Você passou, e foi acima da média!")
else:
    print(f"A média final é {media:.2f}. Infelizmente você não passou :(")

# Faça um Programa que converta metros para centímetros.

informarMetro = float(input("Digite o tamanho em metros: "))

conversao = informarMetro * 100

print(f"{informarMetro:.2f} metros equivalem a {conversao:.2f} centímetros!")

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Digite o raio do círculo: "))
calculoDaArea = 3.14*(raio**2)

print(f"O raio aproximado do círculo é {raio:.2f}, portanto sua área aproximada é {calculoDaArea:.2f}")
print(f"O raio exato do círculo é {raio}, portanto sua área exata é {calculoDaArea}")

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

informarLado = float(input("Digite o valor do lado do quadrado: "))
calculoDeArea = informarLado * 2
dobroDaArea = calculoDeArea * 2

print(f"O dobro da área do quadrado informado é {dobroDaArea:.2f}")

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhoPorHora = float(input("Quanto você ganha por hora? "))
horasTrabalhadasPorMes = float(input(f"Já sabemos que você ganha R$ {ganhoPorHora:.2f} por hora. Agora, nos diga: quantas horas você trabalha por mês? "))
calculoDoSalário = ganhoPorHora * horasTrabalhadasPorMes

if(horasTrabalhadasPorMes > 744):
    print("O máximo de horas trabalhadas em um mês é 744 horas! Rode o código novamente e informe um valor válido!")
else:
    print("Então, você ganha R$ {:.2f} reais por mês!".format(calculoDoSalário))


# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

grauFahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
conversaoCelcius = 5 * ((grauFahrenheit-32)/9)

print("A temperatura em graus Celcius é de {:.2f}°C".format(conversaoCelcius))


# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

grauCelcius = float(input("Digite a temperatura em Celcius: "))
conversaoFahrenheit = ((grauCelcius * 9) / 5) + 32

print("A temperatura em Celcius informada é {}°C. E convertendo para Fahrenheit fica {}°F".format(grauCelcius, conversaoFahrenheit))

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

inteiro1 = int(input("Digite um número inteiro: "))
inteiro2 = int(input("Digite outro número inteiro: "))
numeroReal = float(input("Digite qualquer número real: "))

produto = (inteiro1 * 2) * (inteiro2 / 2)
soma = (inteiro1 * 3) + numeroReal
potenciacao = numeroReal ** 3

print("O primeiro resultado é {:.2f}, o segundo é {:.2f} e o terceiro é {:.2f}.".format(produto, soma, potenciacao))

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Sua altura: "))
achismo = float(input(f"Sabemos que sua altura é {altura}m. E quanto você acha que seria seu peso ideal? "))
calculoPesoIdeal = (72.7*altura) - 58

print("Você disse que sua altura é {}m e que seu peso ideal seria {}kg. E, pelos nossos cálculos, seu peso ideal é {:.2f}kg".format(altura, achismo, calculoPesoIdeal))

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input("Digite sua altura: "))
sexoDaPessoa = input("Você é homem ou mulher (escreva por extenso): ")
pesoHomem = (72.7 * h) - 58
pesoMulher = (62.1 * h) - 44.7

if(sexoDaPessoa == "homem"):
    print(f"Como você é do sexo masculino, seu peso ideal é {pesoHomem:.2f}kg")
else: 
    print(f"Como você é do sexo feminino, seu peso ideal é {pesoMulher:.2f}kg")

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Digite o peso do peixe: "))
excesso = peso - 50
multa = excesso * 4

if(peso > 50):
    print(f"Você excedeu o peso máximo em {excesso:.2f}kg, sua multa é R$ {multa:.2f}")
else:
    print("Você não excedeu o peso máximo!")


# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

ganhoPorHora = float(input("Quanto você ganha por hora? "))
numeroDeHoras = float(input("Quantas horas você trabalha no mês? "))
salarioDoMês = ganhoPorHora * numeroDeHoras

impostoDeRenda = salarioDoMês * (11/100)
inss = salarioDoMês * (8/100)
sindicato = salarioDoMês * (5/100)
totalDescontos = impostoDeRenda + inss + sindicato
salarioLiquido = salarioDoMês - totalDescontos

if(numeroDeHoras > 744):
    print("O número máximo de horas trabalhadas em um mês é 744 horas! Reinicie o código e informe algo válido!")
else:
    print("Seu salário total bruto é de R$ {}. Você paga R$ {} ao INSS, R$ {} ao sindicato e R$ {:.2f} de Imposto de Renda. Portanto, seu salário líquido do mês é R$ {}".format(salarioDoMês, inss, sindicato, impostoDeRenda, salarioLiquido))

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metrosQuadrados = float(input("Digite o tamanho em metros quadrados: "))
calculoCoberturaUmaLata = (18/3)
calculoLatas = metrosQuadrados / calculoCoberturaUmaLata
calculoValor = calculoLatas * 80

print("A quantidade de latas de tinta a serem compradas é de {:.1f}, e o valor total é de R$ {:.2f}".format(calculoLatas, calculoValor))


# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;


# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

metrosQuadrados = float(input("Digite o tamanho em metros quadrados: "))

litros = metrosQuadrados / 6

litros += litros * (10/100)

latas = math.ceil(litros/18)
galoes = math.ceil(litros/3.6)
valorTotalLatas = 80 * latas
valorTotalGaloes = 25 * galoes

print("Com latas de 18L, você precisará de {} lata(s) e gastará R$ {:.2f}.".format(latas, valorTotalLatas))
print("Com galoes de 3.6L, você precisará de {} galõe(s) e gastará R$ {:.2f}.".format(galoes, valorTotalGaloes))

latasMistura = int(litros // 18)
resto = litros % 18
galoesMistura = math.ceil(resto / 3.6)

if(resto > 0 and resto <= 10.8):
    galoesMistura = 1
elif(resto > 10.8 and resto <= 21.6):
    galoesMistura = 2

valorLatasTotal = latasMistura*80
valorGaloesTotal = galoesMistura*25
valorTotalDaCompra = valorLatasTotal + valorGaloesTotal

# print("Você precisará de {} lata(s) e de {} galão(ões). E o valor total ficará em R$ {:.2f}".format(latasMistura, galoesMistura, valorTotalDaCompra))

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Qual é o tamanho do seu arquivo (em MB)? "))
velocidade = float(input("Qual a velocidade do link da internet (em Mbps)? "))

calculoTempo = tamanho / (velocidade/8)

transformaMinutos = calculoTempo / 60

print("O tempo, em minutos, para o download do arquivo será de {:.2f} minutos".format(transformaMinutos))








