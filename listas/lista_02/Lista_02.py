import math

def cabecalho():
    print("*" * 60)
    print("Faculdade Estadual Piauí Instituto de Tecnologia - PIT".center(60))
    print("Bacharelado em Inteligência Artificial".center(60))
    print("Disciplina: Algoritmos e Estruturas de Dados I".center(60))
    print("Prof. João Vagner".center(60))
    print("Aluno: Breno Igo B. P. de Araújo".center(60))
    print("*" * 60)
    print()
    print("ATIVIDADE 02 - Comandos de decisão".center(60))
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
    print("1. Faça um algoritmo que realize a leitura de um valor numérico inteiro qualquer e apresente-o caso não seja maior do que 10.")
    print()

    valor = ler_numero_inteiro("Por favor, digite um valor numérico inteiro: ")

    if valor <= 10:
        print()
        print(f"Valor informado: {valor}")
        print()
    else:
        print()
        print("O valor é maior que 10, portanto não será apresentado.")
        print()

def questao_2():
    print()
    print("2. Faça um algoritmo que dado um valor numérico, diga se ele é par ou impar.")
    print()

    valor = ler_numero_inteiro("Por favor, digite um valor numérico inteiro: ")

    if valor % 2 == 0:
        print()
        print(f"O número {valor} é PAR.")
        print()
    else:
        print()
        print(f"O número {valor} é ÍMPAR.")
        print()

def questao_3():
    print()
    print("3. Faça um algoritmo que dados dois números, apresente-os em ordem crescente.")
    print()

    num_1 = ler_numero_float("Por favor, digite o primeiro número: ")
    num_2 = ler_numero_float("Por favor, digite o segundo número: ")
        
    menor = min(num_1, num_2)
    maior = max(num_1, num_2)

    print()
    print(f"Ordem crescente: {menor}, {maior}")
    print()

def questao_4():
    print()
    print("4. Faça um algoritmo que efetue a leitura de três valores inteiros desconhecidos representados pelas variáveis A, B e C. Em seguida, some os valores fornecidos e apresente o resultado caso a soma seja maior ou igual a 100.")
    print()
    
    A = ler_numero_inteiro("Por favor, digite o valor de A: ")
    B = ler_numero_inteiro("Por favor, digite o valor de B: ")
    C = ler_numero_inteiro("Por favor, digite o valor de C: ")
    
    soma = A + B + C
    
    if soma >= 100:
        print()
        print(f"A soma dos três valores é {soma}, que é maior ou igual a 100.")
        print()
    else:
        print()
        print("O resultado não será apresentado por ser menor que 100.")
        print()

def questao_5():
    print()
    print("5. Faça um algoritmo que leia um número inteiro qualquer e multiplique-o por dois. Apresente o resultado da multiplicação se o resultado for maior que 30.")
    print()

    num = ler_numero_inteiro("Por favor, digite um número inteiro: ")
    resultado = num * 2
    
    if resultado > 30:
        print()
        print(f"O resultado da multiplicação é {resultado}, que é maior que 30.")
        print()
    else:
        print()
        print("O resultado não é maior que 30.")
        print()

def questao_6():
    print()
    print("6. Faça um algoritmo que leia a idade e o nome de uma pessoa que passará por um exame de seleção. Imprima o nome dessa pessoa e a mensagem “Aceita”, caso ela tenha menos que 25 anos.")
    print()
    
    nome = input("Por favor, digite o nome da pessoa: ")
    idade = ler_numero_inteiro("Por favor, digite a idade da pessoa: ")

    if idade < 25:
        print()
        print(f"Nome: {nome} - Aceita")
        print()
    else:
        print()
        print(f"Nome: {nome} - Não Aceita (idade igual ou superior a 25 anos)")
        print()

def questao_7():
    print()
    print("7.Faça um algoritmo que leia um número inteiro qualquer. Se o número lido for negativo, escreva a mensagem “Número invalido”. Senão escreva a mensagem: “Número válido”.")
    print()

    num = ler_numero_inteiro("Por favor, digite um número inteiro: ")
    
    if num < 0:
        print()
        print("Número invalido")
        print()
    else:
        print()
        print("Número válido")
        print()

def questao_8():
    print()
    print("8. Faça um algoritmo que receba um número qualquer e imprima o quadrado desse número caso ele seja positivo, e a raiz quadrada caso seja negativo.")
    print()

    num = ler_numero_float("Por favor, digite um número: ")
    
    if num > 0:
        print()
        print(f"O número é positivo. O quadrado de {num} é {num**2:.2f}")
        print()
    elif num < 0:
        raiz = math.sqrt(abs(num))
        print()
        print(f"O número é negativo. A raiz quadrada do seu valor absoluto é {raiz:.2f} (no conjunto dos complexos: {raiz:.2f}i)")
        print()
    else:
        print()
        print("O número é zero.")
        print()

def questao_9():
    print()
    print("9. Faça um algoritmo que indique se um número digitado está compreendido entre 20 e 90 ou não (20 e 90 não estão na faixa de valores).")
    print()
    
    num = ler_numero_float("Por favor, digite um número: ")

    if 20 < num < 90:
        print()
        print(f"O número {num} ESTÁ compreendido entre 20 e 90.")
        print()
    else:
        print()
        print(f"O número {num} NÃO ESTÁ compreendido entre 20 e 90.")
        print()

def questao_10():
    print()
    print("10. Faça um algoritmo que leia dois números e imprima o quadrado do menor número e raiz quadrada do maior número. Caso os dois números forem iguais, apresente o cubo deles.")
    print()

    n1 = ler_numero_float("Por favor, digite o primeiro número: ")
    n2 = ler_numero_float("Por favor, digite o segundo número: ")
    
    if n1 == n2:
        print()
        print(f"Os números são iguais. O cubo deles é: {n1**3:.2f}")
        print()
    else:
        menor = min(n1, n2)
        maior = max(n1, n2)
        print()
        print(f"O quadrado do menor ({menor}) é: {menor**2:.2f}")
        if maior >= 0:
            print(f"A raiz quadrada do maior ({maior}) é: {math.sqrt(maior):.2f}")
            print()
        else:
            print(f"Não é possível calcular a raiz real do maior número pois ele é negativo.")
            print()

def questao_11():
    print()
    print("Faça um algoritmo que leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.")
    print()

    n1 = ler_numero_float("Por favor, digite o primeiro número: ")
    n2 = ler_numero_float("Por favor, digite o segundo número: ")

    soma = n1 + n2
    
    if soma > 20:
        resultado = soma + 8
        print()
        print(f"Soma ({soma}) > 20. Resultado final (+8): {resultado:.2f}")
        print()
    else:
        resultado = soma - 5
        print()
        print(f"Soma ({soma}) <= 20. Resultado final (-5): {resultado:.2f}")
        print()

def questao_12():
    print()
    print("12. Faça um algoritmo que receba o salário de um trabalhador e o valor da prestação de um empréstimo e faça:")
    print("Se a prestação for maior que 20% do salário, imprima: Empréstimo não concebido; caso contrário, imprima: Empréstimo concebido.")
    print()
    
    salario = ler_numero_float("Por favor, digite o salário do trabalhador: R$ ")
    prestacao = ler_numero_float("Por favor, digite o valor da prestação: R$ ")
    
    if prestacao > (salario * 0.20):
        print()
        print("Empréstimo não concebido")
        print()
    else:
        print()
        print("Empréstimo concebido")
        print()

def questao_13():
    print()
    print("13. Faça um algoritmo para verificar se determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente pelos dois.")
    print()
    
    num = ler_numero_inteiro("Por favor, digite um número inteiro: ")
    
    div_3 = (num % 3 == 0)
    div_5 = (num % 5 == 0)
    
    if div_3 != div_5:
        print()
        print(f"O número {num} atende à condição (é divisível por 3 ou 5, mas não por ambos).")
        print()
    else:
        print()
        print(f"O número {num} NÃO atende à condição.")
        print()

def questao_14():
    print()
    print("14. Faça um algoritmo que dados três números apresente-os em ordem crescentes..")
    print()

    n1 = ler_numero_float("Por favor, digite o 1º número: ")
    n2 = ler_numero_float("Por favor, digite o 2º número: ")
    n3 = ler_numero_float("Por favor, digite o 3º número: ")
    
    numeros = [n1, n2, n3]
    numeros.sort()

    print()
    print(f"Ordem crescente: {numeros[0]}, {numeros[1]}, {numeros[2]}")
    print()

def questao_15():
    print()
    print("15. Faça um algoritmo que dados à altura (h) e o sexo de uma pessoa (M - masculino e F - feminino), calcule seu peso ideal, utilizando as seguintes fórmulas:")
    print("Para homens: (72.7 * h) - 58")
    print("Para mulheres: (62.1 * h) - 47")
    print()

    altura = ler_numero_float("Por favor, digite a altura (ex: 1.75): ")
    sexo = input("Por favor, digite o sexo (M/F): ").strip().upper()
    
    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
        print()
        print(f"O peso ideal para um homem de {altura}m é {peso_ideal:.2f} kg")
        print()
    elif sexo == 'F':
        peso_ideal = (62.1 * altura) - 47
        print()
        print(f"O peso ideal para uma mulher de {altura}m é {peso_ideal:.2f} kg")
        print()
    else:
        print()
        print("Sexo inválido. Por favor, digite M ou F.")
        print()

def questao_16():
    print()
    print("Um comerciante comprou um produto e deseja revendê-lo com um lucro de 45% se o valor de compra for menor do que R$ 20,00; caso contrário, o lucro será de 30%. Entrar com o valor de compra do produto e exibir seu valor de venda.")
    print()

    valor_compra = ler_numero_float("Por favor, digite o valor de compra: R$ ")
    
    if valor_compra < 20.00:
        valor_venda = valor_compra * 1.45
    else:
        valor_venda = valor_compra * 1.30
        
    print()
    print(f"O valor de venda do produto será: R$ {valor_venda:.2f}")
    print()

def questao_17():
    print()
    print("17. Dada a idade de um jogador de futebol classifique-o em uma das seguintes categorias:")
    print("Infantil A: 5 a 7 anos")
    print("Infantil B: 8 a 10 anos")
    print("Juvenil A: 11 a 13 anos")
    print("Juvenil B: 14 a 17 anos")
    print("Caso contrário, não pertence a nenhuma categoria.")


    idade = ler_numero_inteiro(" Por favor, digite a idade do jogador: ")
    
    if 5 <= idade <= 7:
        print()
        print("Categoria: Infantil A")
        print()
    elif 8 <= idade <= 10:
        print()
        print("Categoria: Infantil B")
        print()
    elif 11 <= idade <= 13:
        print()
        print("Categoria: Juvenil A")
        print()
    elif 14 <= idade <= 17:
        print()
        print("Categoria: Juvenil B")
        print()
    else:
        print()
        print("Não pertence a nenhuma categoria.")
        print()

def questao_18():
    print()
    print("Dado o salário bruto de uma pessoa, exibir o desconto do INSS segundo a tabela abaixo:")
    print("Até R$ 600,00: Isento")
    print("De R$ 600,01 a R$ 1.200,00: 20%")
    print("De R$ 1.200,01 a R$ 2.000,00: 25%")
    print("Acima de R$ 2.000,00: 30%")
    print()

    salario = ler_numero_float("Por favor, digite o salário bruto: R$ ")
    
    if salario <= 600.00:
        print()
        print("Desconto INSS: Isento")
        print()
    elif 600.00 < salario <= 1200.00:
        desconto = salario * 0.20
        print()
        print(f"Desconto INSS (20%): R$ {desconto:.2f}")
        print()
    elif 1200.00 < salario <= 2000.00:
        desconto = salario * 0.25
        print()
        print(f"Desconto INSS (25%): R$ {desconto:.2f}")
        print()
    else:
        desconto = salario * 0.30
        print()
        print(f"Desconto INSS (30%): R$ {desconto:.2f}")
        print()

def questao_19():
    print()
    print("19. Faça um algoritmo que leia o ano atual e o ano de nascimento de uma pessoa. Em seguida, escreva uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).")
    print("Não é eleitor (abaixo de 16 anos);")
    print("Eleitor obrigatório (entre 18 e 65 anos);")
    print("Eleitor facultativo (entre 16 e 18 anos ou acima de 65 anos).")


    ano_atual = ler_numero_inteiro("Por favor, digite o ano atual: ")
    ano_nascimento = ler_numero_inteiro("Por favor, digite o ano de nascimento: ")
    
    idade = ano_atual - ano_nascimento
    print()
    print(f"A idade estimada é {idade} anos.")
    
    if idade < 16:
        print("Situação: Não é eleitor")
        print()
    elif 18 <= idade <= 65:
        print("Situação: Eleitor obrigatório")
        print()
    else:
        print("Situação: Eleitor facultativo")
        print()

def questao_20():
    print()
    print("Faça um algoritmo que dada a idade de uma pessoa, determine sua classificação segundo a seguinte tabela")
    print("Maior de idade;")
    print("Menor de idade;")
    print("Pessoa idosa (idade superior ou igual a 65 anos).")
    print()

    idade = ler_numero_inteiro("Por favor, digite a idade da pessoa: ")
    
    if idade < 18:
        print()
        print("Classificação: Menor de idade")
        print()
    elif 18 <= idade < 65:
        print()
        print("Classificação: Maior de idade")
        print()
    else:
        print()
        print("Classificação: Pessoa idosa")
        print()

def questao_21():
    print()
    print("21. Faça um algoritmo em que receba o valor de x, e calcule e imprima o valor de f(x)")
    print("f(x) = 1, se x <= 1")
    print("f(x) = 2, se 1 < x <= 2")
    print("f(x) = x^2, se 2 < x <= 3")
    print("f(x) = x^3, se x > 3")
    print()

    x = ler_numero_float("Por favor, digite o valor de x: ")
    
    if x <= 1:
        fx = 1
    elif 1 < x <= 2:
        fx = 2
    elif 2 < x <= 3:
        fx = x**2
    else:
        fx = x**3
        
    print()
    print(f"O valor de f({x}) é: {fx:.2f}")
    print()

def questao_22():
    print()
    print("22. Uma loja oferece para os seus clientes, um determinado desconto de acordo com o valor da compra efetuada. O desconto é de 10%, se o valor da compra for até R$200.00, 15% se for maior que R$ 200 e menor ou igual a R$ 500,00 e 20% se for acima de R$ 500,00. Crie um algoritmo que leia o nome do cliente e o valor da compra. Mostre ao final o nome do cliente, o valor da compra, o percentual de desconto e o seu valor e valor total a pagar deste cliente.")
    print()

    nome = input("Por favor, digite o nome do cliente: ")
    valor_compra = ler_numero_float("Por favor, digite o valor da compra: R$ ")
    
    if valor_compra <= 200.00:
        perc_desconto = 10
    elif 200.00 < valor_compra <= 500.00:
        perc_desconto = 15
    else:
        perc_desconto = 20
        
    valor_desconto = valor_compra * (perc_desconto / 100)
    total_pagar = valor_compra - valor_desconto
    
    print()
    print(f"Cliente: {nome}")
    print(f"Valor original da compra: R$ {valor_compra:.2f}")
    print(f"Percentual de desconto: {perc_desconto}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor TOTAL a pagar: R$ {total_pagar:.2f}")
    print()

def questao_23():
    print()
    print("23. Faça um programa que informe o mês de acordo com o numero informado pelo usuário.")
    print("Exemplo:")
    print("Entrada: 4.")
    print(" Saída: Abril.")
    print()

    mes = ler_numero_inteiro("Por favor, digite o número do mês (1 a 12): ")
    
    meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
    
    if mes in meses:
        print()
        print(f"Saída: {meses[mes]}")
        print()
    else:
        print()
        print("Número de mês inválido.")
        print()

def menu():
    while True:
        cabecalho()
        print("Menu para acesso às 23 Questões da Lista 02 (Condicionais)".center(60))
        print("=" * 60)
        print()

        for i in range(1, 24):
            print(f"{i}. Questão {i}")
        print("0. Sair")

        escolha = ler_numero_inteiro("Por favor, escolha uma opção (1-23) ou 0 para sair: ")

        if escolha == 0:
            print()
            print("Obrigado por usar! Até breve.")
            print()
            break
        elif 1 <= escolha <= 23:
            print()
            print(f"Você escolheu a Questão {escolha}.")
            questao_func = globals().get(f"questao_{escolha}")
            if questao_func:
                questao_func()
                        
            input("Pressione ENTER para voltar ao menu...")
            print()
            print()
            
        else:
            print()
            print("Questão não encontrada. Por favor, tente novamente.")
            print()

if __name__ == "__main__":
    menu()