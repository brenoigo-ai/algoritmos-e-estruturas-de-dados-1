def cabecalho():
    print("*" * 60)
    print("Faculdade Estadual Piauí Instituto de Tecnologia - PIT".center(60))
    print("Bacharelado em Inteligência Artificial".center(60))
    print("Disciplina: Algoritmos e Estruturas de Dados I".center(60))
    print("Prof. João Vagner".center(60))
    print("Aluno: Breno Igo B. P. de Araújo".center(60))
    print("*" * 60)
    print()
    print("ATIVIDADE 01".center(60))
    print()

def ler_numero_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(',','.'))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def ler_numero_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")  
    
def questao_1():
    print()
    print("1. Faça um programa que receba o valor pago, o valor que é o preço do produto e retorne o troco a ser dado.")
    print()

    valor_pago = ler_numero_float("Digite o valor pago: R$ ")
    preco_produto = ler_numero_float("Digite o preço do produto: R$ ")
    troco = valor_pago - preco_produto
    print()
    print(f"O troco a ser dado é: R$ {troco:.2f}")
    print()

def questao_2():
    print()
    print("2. Faça um programa que receba o valor do quilo de um produto e a quantidade de quilos do produto consumida calculando o valor final a ser pago.")
    print()

    valor_kg = ler_numero_float("Digite o valor do quilo do produto: R$ ")
    quantidade_kg = ler_numero_float("Digite a quantidade de quilos consumida do produto: ")

    valor_final = valor_kg * quantidade_kg

    print()
    print(f"O valor final a ser pago é: R$ {valor_final:.2f}")
    print()

def questao_3():
    print()
    print("3. Faça um algoritmo que receba dois números e exiba o resultado da sua soma.")
    print()

    num_1 = ler_numero_float("Por favor, digite o primeiro número: ")
    num_2 = ler_numero_float("Por favor, digite o segundo número: ")

    soma = num_1 + num_2

    print()
    print(f"A soma dos dois números informados pelo usuário é: {num_1} + {num_2} = {soma}")
    print()

def questao_4():
    print()
    print("4. Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, multiplicação e a divisão dos números lidos.")
    print()

    num_1 = ler_numero_float("Por favor, digite o primeiro número: ")
    num_2 = ler_numero_float("Por favor, digite o segundo número: ")

    soma = num_1 + num_2
    subtracao = num_1 - num_2
    multiplicacao = num_1 * num_2
    
    print()
    print(f"A soma dos dois números informados pelo usuário é: {num_1} + {num_2} = {soma:.2f}")
    print(f"A subtração dos dois números informados pelo usuário é: {num_1} - {num_2} = {subtracao:.2f}")
    print(f"A multiplicação dos dois números informados pelo usuário é: {num_1} * {num_2} = {multiplicacao}")

    if num_2 != 0:
        divisao = num_1 / num_2
        print()
        print(f"A divisão dos dois números informados pelo usuário é: {num_1} / {num_2} = {divisao:.2f}")
        print()

    else:
        print()
        print("Não é possível realizar a divisão, pois o segundo número informado é igual a zero.")
        print()

def questao_5():
    print()
    print("5. Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto.")
    print()

    distancia_total = ler_numero_float("Por favor, digite a distância total percorrida pelo carro em km: ")
    combustivel_gasto = ler_numero_float("Por favor, digite o total de combustível gasto em litros: ")

    if combustivel_gasto > 0:
         consumo_medio = distancia_total / combustivel_gasto
         print()
         print(f"O consumo médio do automóvel é: {consumo_medio:.2f} km/l")
         print()
    else:
        print()
        print("O valor do combustível gasto não pode ser menor ou igual a zero.")
        print()

def questao_6():
    print()
    print("6. Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 5% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.")
    print()

    nome_vendedor = input("Por favor, digite o nome do vendedor: ")
    salario_fixo = ler_numero_float("Por favor, digite o salário fixo do vendedor: R$ ")
    total_vendas = ler_numero_float("Por favor, digite o valor em dinheiro do total de vendas efetuadas pelo vendedor no mês: R$ ")

    comissao = total_vendas * 0.05
    salario_final = salario_fixo + comissao

    print()
    print(f"Nome do vendedor: {nome_vendedor}")
    print(f"Salário fixo: R$ {salario_fixo:.2f}")
    print(f"Salário final no mês (com comissão): R$ {salario_final:.2f}")
    print()

def questao_7():
    print()
    print("7. Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).")
    print()

    nome = input("Por favor, digite o nome do aluno: ")
    nota_1 = ler_numero_float("Por favor, digite a nota da primeira prova: ")
    nota_2 = ler_numero_float("Por favor, digite a nota da segunda prova: ")
    nota_3 = ler_numero_float("Por favor, digite a nota da terceira prova: ")

    media_aritmetica = (nota_1 + nota_2 + nota_3) / 3

    print()
    print(f"Nome do aluno: {nome}")
    print(f"Média aritmética das notas: {media_aritmetica:.2f}")
    print()

def questao_8():
    print()
    print("8. Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.")
    print()

    A = input("Por favor, digite o valor da variável A: ")
    B = input("Por favor, digite o valor da variável B: ")

    print()
    print(f"Os valores antes da troca são: A = {A} e B = {B}")
    A, B = B, A
    print()
    print(f"Os valores depois da troca são: A = {A} e B = {B}")
    print()

def questao_9():
    print()
    print("9. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é: F=(9*C+160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.")
    print()

    c = ler_numero_float("Por favor, digite a temperatura em graus Celsius: ")
    f = (9 * c + 160) / 5

    print()
    print(f"Dado a temperatura {c} °C, a temperatura em graus Fahrenheit é: {f} °F")
    print()

def questao_10():
    print()
    print("10.Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.")
    print()

    cot_dolar = ler_numero_float("Por favor, digite o valor atual da cotação do dólar: R$ ")
    quant_dolares = ler_numero_float("Por favor, digite a quantidade de dólares que você possui: US$ ")

    valor_real = cot_dolar * quant_dolares

    print()
    print(f"O valor em real (R$) da quantidade de dólares informada pelo usuário em relação ao valor da cotação do dólar informada é: R$ {valor_real:.2f}")
    print()

def questao_11():
    print()
    print("11. Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,50% a. m.")
    print()

    valor = ler_numero_float("Por favor, digite o valor que será depositado: R$ ")
    
    montante = valor * 1.005

    print()
    print(f"Ao depositar o valor de R$ {valor:.2f}, o montante após um mês com rendimento de 0,50% a.m. será: R$ {montante:.2f}")
    print()

def questao_12():
    print()
    print("12.Uma loja está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.")
    print()

    valor_compra = ler_numero_float("Por favor, digite o valor da compra: R$ ")

    valor_prestacao = valor_compra / 5

    print()
    print(f"É possível parcelar o valor da compra de R$ {valor_compra:.2f} em 5 prestações de R$ {valor_prestacao:.2f} sem juros.")
    print()

def questao_13():
    print()
    print("13.Escreva um algoritmo que leia um número inteiro e imprima o seu sucessor e seu antecessor.")
    print()

    numero = ler_numero_inteiro("Por favor, digite um número inteiro: ")

    sucessor = numero + 1
    antecessor = numero - 1

    print()
    print(f"Dado o número inteiro {numero}, o seu sucessor é: {sucessor} e o seu antecessor é: {antecessor}")
    print()

def questao_14():
    print()
    print("14.Escreva um algoritmo que leia dois números inteiros e imprima o resultado da soma destes dois valores. Antes do resultado, deve ser impressa a seguinte mensagem 'SOMA'.")
    print()

    num_1 = ler_numero_inteiro("Por favor, digite o primeiro número inteiro: ")
    num_2 = ler_numero_inteiro("Por favor, digite o segundo número inteiro: ")

    soma = num_1 + num_2

    print()
    print(f"SOMA: {num_1} + {num_2} = {soma}")
    print()

def questao_15():
    print()
    print("15.Escreva um algoritmo que leia um número real e imprima a terça parte deste número.")
    print()

    numero_real = ler_numero_float("Por favor, digite um número real: ")

    terca_parte = numero_real / 3

    print()
    print(f"A terça parte do número real {numero_real} é: {terca_parte:.2f}")
    print()

def questao_16():
    print()
    print("16.Escreva um algoritmo que leia dois números reais e imprima a média aritmética entre esses dois valores com a seguinte mensagem 'MEDIA' antes do resultado.")
    print()

    num_1 = ler_numero_float("Por favor, digite o primeiro número real: ")
    num_2 = ler_numero_float("Por favor, digite o segundo número real: ")

    media = (num_1 + num_2) / 2

    print()
    print(f"MEDIA: A média aritmética entre os números reais {num_1} e {num_2} é: {media:.2f}")

def questao_17():
    print()
    print("17.Faça um programa que receba 2 valores e retorne o maior entre eles.")
    print()

    valor_1 = ler_numero_float("Por favor, digite o primeiro valor: ")
    valor_2 = ler_numero_float("Por favor, digite o segundo valor: ")

    while True:
        if valor_1 > valor_2:
            print()
            print(f"O maior valor entre {valor_1} e {valor_2} é: {valor_1}")
            print()
            break
        elif valor_2 > valor_1:
            print()
            print(f"O maior valor entre {valor_1} e {valor_2} é: {valor_2}")
            print()
            break
        else:
            print()
            print("Os valores informados são iguais.")
            print()
            break

def questao_18():
    print()
    print("18.Faça um programa que receba 4 valores e retorne o menor entre eles.")
    print()

    valor_1 = ler_numero_float("Por favor, digite o primeiro valor: ")
    valor_2 = ler_numero_float("Por favor, digite o segundo valor: ")
    valor_3 = ler_numero_float("Por favor, digite o terceiro valor: ")
    valor_4 = ler_numero_float("Por favor, digite o quarto valor: ")

    menor_valor = min(valor_1, valor_2, valor_3, valor_4)

    print()
    print(f"O menor valor entre {valor_1}, {valor_2}, {valor_3} e {valor_4} é: {menor_valor}")
    print()

def questao_19():
    print()
    print("19.Faça um programa que receba 3 valores que representarão os lados de um triângulo e verifique se os valores formam um triângulo e classifique esse triângulo como:")
    print("◦ Equilátero (3 lados iguais)")
    print("◦ Isósceles (2 lados iguais)")
    print("◦ Escaleno (3 lados diferentes)")
    print("Lembre-se que para formar um triângulo:")
    print("◦ Nenhum dos lados pode ser igual a zero;")
    print("◦ Um lado não pode ser maior do que a soma dos outros dois;")
    print()

    while True:
        valor_1 = ler_numero_float("Por favor, digite o valor do primeiro lado do triângulo: ")
        valor_2 = ler_numero_float("Por favor, digite o valor do segundo lado do triângulo: ")
        valor_3 = ler_numero_float("Por favor, digite o valor do terceiro lado do triângulo: ")

        if valor_1 <= 0 or valor_2 <= 0 or valor_3 <= 0:
            print()
            print("Não é possível formar um triângulo, pois um dos lados é igual ou menor que zero.")
            print()
            continue

        elif (valor_1 + valor_2 <= valor_3) or (valor_1 + valor_3 <= valor_2) or (valor_2 + valor_3 <= valor_1):
            print()
            print("Não é possível formar um triângulo, pois um dos lados é maior do que a soma dos outros dois.")
            print()
            continue

        else:
            if valor_1 == valor_2 == valor_3:
                print()
                print("Os valores informados formam um triângulo Equilátero (3 lados iguais).")
                print()
                break

            elif valor_1 == valor_2 or valor_1 == valor_3 or valor_2 == valor_3:
                print()
                print("Os valores informados formam um triângulo Isósceles (2 lados iguais).")
                print()
                break

            else:
                print()
                print("Os valores informados formam um triângulo Escaleno (3 lados diferentes).")
                print()
                break

def questao_20():
    print()
    print("20.Utilize a estrutura if para fazer um programa que retorne o nome de um produto a partir do código do mesmo. Considere os seguintes códigos:")
    print("◦ 001=Parafuso")
    print("◦ 002=Porca")
    print("◦ 003=Prego")
    print("◦ Para qualquer outro código indicar: Diversos.")
    print()

    codigo_produto = input("Por favor, digite o código do produto (001, 002 ou 003): ")

    if codigo_produto == "001":
        print()
        print("O produto correspondente ao código 001 é: Parafuso")
        print()
    
    elif codigo_produto == "002":
        print()
        print("O produto correspondente ao código 002 é: Porca")
        print()

    elif codigo_produto == "003":
        print()
        print("O produto correspondente ao código 003 é: Prego")
        print()

    else:
        print()
        print("Diversos")
        print()

def questao_21():
    print()
    print("21.Escreva um algoritmo que leia um número e o imprima caso ele seja maior que 20.")
    print()

    numero = ler_numero_float("Por favor, digite um número: ")

    if numero > 20:
        print()
        print(f"O número informado ({numero}) é maior que 20.")
        print()

    else:
        print()
        print("O número não será impresso, haja vista ser igual ou menor que 20.")
        print()

def questao_22():
    print()
    print("22.Construa um algoritmo que leia dois valores numéricos inteiros e efetue a adição; caso o resultado seja maior que 10, apresentá-lo.")
    print()

    valor_1 = ler_numero_inteiro("Por favor, digite o primeiro valor inteiro: ")
    valor_2 = ler_numero_inteiro("Por favor, digite o segundo valor inteiro: ")

    soma = valor_1 + valor_2

    if soma > 10:
        print()
        print(f"A soma dos valores informados ({soma}) é maior que 10.")
        print()
    else:
        print()
        print("A soma do valor não será informado, haja vista ser igual ou menor que 10.")
        print()

def questao_23():
    print()
    print("23.Escreva um algoritmo para determinar se um dado número N (recebido através do teclado) é POSITIVO, NEGATIVO ou NULO.")
    print()

    n = ler_numero_float("Por favor, atribua um valor para o número N: ")

    if n > 0:
        print()
        print("O número N é POSITIVO.")
        print()
    elif n < 0:
        print()
        print("O número N é NEGATIVO.")
        print()
    else:
        print()
        print("O número N é NULO.")
        print()

def questao_24():
    print()
    print("24.Construir um algoritmo que leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.")
    print()

    num_1 = ler_numero_float("Por favor, digite o primeiro número: ")
    num_2 = ler_numero_float("Por favor, digite o segundo número: ")

    soma = num_1 + num_2

    if soma > 20:
        resultado = soma + 8
        print()
        print(f"O valor somado ({soma}) é maior que 20, portanto o resultado final será: {resultado}")
        print()

    else:
        resultado = soma - 5
        print()
        print(f"O valor somado ({soma}) é menor ou igual a 20, portanto o resultado final será: {resultado}")
        print()

def questao_25():
    print()
    print("25.Escreva um algoritmo que leia um número e imprima o quadrado do número caso ele seja negativo.")
    print()

    numero = ler_numero_float("Por favor, digite um número: ")

    if numero < 0:
        quadrado = numero ** 2
        print()
        print(f"O número informado ({numero}) é negativo, portanto o seu quadrado é: {quadrado}")
        print()

    else:
        print()
        print("O número informado não é negativo, portanto não será impresso.")
        print()

def menu():
    while True:
        cabecalho()

        print()
        print("Menu para acesso às 25 Questões da disciplina Algoritmos e Estruturas de Dados I do Bacharelado em Inteligência Artificial do Piauí Instituto de Tecnologia - PIT".center(60))
        print()
        print("=" * 60)
        print()

        for i in range(1, 26):
            print(f"{i}. Questão {i}")
        

        escolha = ler_numero_inteiro("Por favor, escolha uma opção para acessar uma questão (1-25) ou 0 para sair: ")

        if escolha == 0:
            print()
            print("Obrigado por usar! Até breve.")
            print()
            break

        elif 1 <= escolha <= 25:
            print()
            print(f"Você escolheu a Questão {escolha}.")
            print()
            questao_func = globals().get(f"questao_{escolha}")
            if questao_func:
                questao_func()
            else:
                print("Questão não encontrada. Por favor, tente novamente.")

            print()
            input("Pressione ENTER para voltar ao menu...")
            print()

if __name__ == "__main__":
    menu()
