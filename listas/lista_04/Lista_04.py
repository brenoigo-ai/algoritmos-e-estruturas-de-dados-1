def cabecalho():
    print("*" * 60)
    print("Faculdade Estadual Piauí Instituto de Tecnologia - PIT".center(60))
    print("Bacharelado em Inteligência Artificial".center(60))
    print("Disciplina: Algoritmos e Estruturas de Dados I".center(60))
    print("Prof. João Vagner".center(60))
    print("Aluno: Breno Igo B. P. de Araújo".center(60))
    print("*" * 60)
    print()
    print("ATIVIDADE 04 - Funções".center(60))
    print()

def ler_numero_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print()
            print("Entrada inválida. Por favor, digite um número válido.")
            print()

def ler_numero_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print()
            print("Entrada inválida. Por favor, digite um número inteiro válido.")
            print()

def verifica_paridade(n):
    if n % 2 == 0:
        return 'p'
    return 'i'

def questao_1():
    print()
    print("1. Faça uma função que receba como parâmetro um número inteiro e retorne o")
    print("caractere 'p' (se o número for par) ou o 'i' (se o número for impar).")
    print()
    num = ler_numero_inteiro("Digite um número inteiro: ")
    resultado = verifica_paridade(num)
    print()
    print(f"Resultado retornado pela função: '{resultado}'")
    print()

def imprimir_boas_vindas(nome):
    print()
    print(f"Seja bem-vindo, {nome}!")
    print()

def questao_2():
    print()
    print("2. Faça uma função que receba um nome de uma pessoa como parâmetro e")
    print("imprima uma mensagem de boas-vindas. Exemplo: Seja bem-vindo, João!")
    print()
    nome = input("Digite seu nome: ")
    imprimir_boas_vindas(nome)

def menor_valor(v1, v2):
    if v1 < v2:
        return v1
    return v2

def questao_3():
    print()
    print("3. Criar uma função que calcule e retorne o MENOR entre dois valores")
    print("recebidos como parâmetro. Um algoritmo para testar tal função deve ser criado.")
    print()
    v1 = ler_numero_float("Digite o primeiro valor: ")
    v2 = ler_numero_float("Digite o segundo valor: ")
    resultado = menor_valor(v1, v2)
    print()
    print(f"O menor valor retornado é: {resultado}")
    print()

def converter_pes_metros(feet):
    return feet / 3.281

def questao_4():
    print()
    print("4. Crie uma função que realize a conversão de pés (feet) para metros (m), onde")
    print("o valor de feet é passado como parâmetro e m é retornado. Sabe-se que 1")
    print("metro está para 3,281 pés.")
    print()
    pes = ler_numero_float("Digite o valor em pés (feet): ")
    metros = converter_pes_metros(pes)
    print()
    print(f"{pes} pés equivalem a {metros:.2f} metros.")
    print()

def calcular_novo_salario(salario, porcentagem):
    return salario * (1 + (porcentagem / 100))

def questao_5():
    print()
    print("5. Faça uma função que receba como parâmetros o valor de um salário e um")
    print("valor em porcentagem. A função deve retornar um novo salário com reajuste")
    print("de aumento no valor da porcentagem.")
    print()
    salario = ler_numero_float("Digite o salário: R$ ")
    porcentagem = ler_numero_float("Digite a porcentagem de aumento (%): ")
    novo = calcular_novo_salario(salario, porcentagem)
    print()
    print(f"O novo salário reajustado é: R$ {novo:.2f}")
    print()

def converter_f_para_c(f):
    return (f - 32) / 1.8

def questao_6():
    print()
    print("6. Crie uma função que realize a conversão de Fahrenheit (F) para graus Celsius")
    print("(C), onde F é passado como parâmetro e C é retornado. C=(F-32)/1.8")
    print()
    f = ler_numero_float("Digite a temperatura em Fahrenheit: ")
    c = converter_f_para_c(f)
    print()
    print(f"A temperatura convertida é: {c:.2f} °C")
    print()

def calcular_retangulo(base, altura):
    perimetro = 2 * (base + altura)
    area = base * altura
    return perimetro, area

def questao_7():
    print()
    print("7. Faça uma função que dados os lados de retângulo como parâmetros,")
    print("apresente: perímetro e área.")
    print()
    base = ler_numero_float("Digite a base do retângulo: ")
    altura = ler_numero_float("Digite a altura do retângulo: ")
    perimetro, area = calcular_retangulo(base, altura)
    print()
    print(f"Perímetro do retângulo: {perimetro}")
    print(f"Área do retângulo: {area}")
    print()

def verificar_divisibilidade(x, y):
    if y != 0 and x % y == 0:
        return 1
    return 0

def questao_8():
    print()
    print("8. Escreva uma função que receba dois números inteiros x e y. Essa função")
    print("deve verificar se x é divisível por y. No caso positivo, a função deve retornar")
    print("1, caso contrário deve retornar 0 (zero).")
    print()
    x = ler_numero_inteiro("Digite o valor de x: ")
    y = ler_numero_inteiro("Digite o valor de y: ")
    resultado = verificar_divisibilidade(x, y)
    print()
    print(f"Resultado retornado: {resultado}")
    print()

def nome_do_mes(mes):
    meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    if mes in meses:
        return meses[mes]
    return "Mês inválido"

def questao_9():
    print()
    print("9. Faça uma função que receba como parâmetro o número de um mês do ano")
    print("e retorne seu nome. Exemplo: 02 = Fevereiro.")
    print()
    mes = ler_numero_inteiro("Digite o número do mês: ")
    nome = nome_do_mes(mes)
    print()
    print(f"Nome retornado: {nome}")
    print()

def procedimento_adicao(a, b):
    soma = a + b
    print()
    if soma > 20:
        print(f"Soma maior que 20. Resultado final: {soma + 8}")
    else:
        print(f"Soma menor ou igual a 20. Resultado final: {soma - 5}")
    print()

def questao_10():
    print()
    print("10. Faça um procedimento em que receba dois números por parâmetro e efetue")
    print("a adição. Caso o valor somado seja maior que 20, este deverá ser")
    print("apresentado somando-se a ele mais 8; caso o valor somado seja menor ou")
    print("igual a 20, este deverá ser apresentado subtraindo-se 5.")
    print()
    n1 = ler_numero_float("Digite o primeiro número: ")
    n2 = ler_numero_float("Digite o segundo número: ")
    procedimento_adicao(n1, n2)

def procedimento_bissexto(ano):
    print()
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")
    print()

def questao_11():
    print()
    print("11. Faça um procedimento que receba o valor de um ano por parâmetro e")
    print("determine se ele é bissexto. Sendo que um ano é bissexto se ele for divisível")
    print("por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988,")
    print("1992, 1996.")
    print()
    ano = ler_numero_inteiro("Digite o ano: ")
    procedimento_bissexto(ano)

def procedimento_tabuada(num):
    print()
    if num > 0:
        for i in range(11):
            print(f"{num} x {i} = {num * i}")
    else:
        print("O número fornecido não é positivo.")
    print()

def questao_12():
    print()
    print("12. Faça um procedimento que dado um número inteiro e positivo por parâmetro,")
    print("exiba sua tabuada de multiplicar (0 a 10).")
    print()
    num = ler_numero_inteiro("Digite um número inteiro positivo: ")
    procedimento_tabuada(num)

def procedimento_intervalo(inf, sup):
    print()
    print("Saída: ", end="")
    for i in range(inf, sup + 1):
        print(i, end=" ")
    print()
    print()

def questao_13():
    print()
    print("13. Faça um procedimento que receba por parâmetro o limite inferior e superior")
    print("de um intervalo e imprima todos os números naturais no intervalo fechado.")
    print("Suponha que os dados digitados são para um intervalo crescente.")
    print("Exemplo:")
    print("Limite inferior: 5")
    print("Limite superior: 12")
    print("Saída: 5 6 7 8 9 10 11 12")
    print()
    inf = ler_numero_inteiro("Limite inferior: ")
    sup = ler_numero_inteiro("Limite superior: ")
    procedimento_intervalo(inf, sup)

def tempo_ultrapassagem(v_fd, v_m, dist):
    v_relativa = v_m - v_fd
    return dist / v_relativa

def questao_14():
    print()
    print("14. Francisco Daniel e Matheus resolveram viajar para o mesmo destino.")
    print("Francisco Daniel está dirigindo a uma velocidade de 80 KM/h e Matheus a")
    print("100 KM/h. Sabe-se que Francisco Daniel está a uma distância de 60 km de")
    print("Matheus. Faça uma função que retorne o tempo em horas que Matheus")
    print("precisará para ultrapassar Francisco Daniel.")
    print()
    v_francisco = 80
    v_matheus = 100
    distancia = 60
    horas = tempo_ultrapassagem(v_francisco, v_matheus, distancia)
    print()
    print(f"O tempo necessário para a ultrapassagem será de {horas} horas.")
    print()

def eh_letra(caractere):
    if caractere.isalpha() and len(caractere) == 1:
        return 1
    return 0

def questao_15():
    print()
    print("15. Criar uma função que determine se um caractere, recebido como parâmetro,")
    print("é ou não uma letra do alfabeto. A função deve retornar 1 caso positivo e 0 em")
    print("caso contrário.")
    print()
    caractere = input("Digite um caractere: ")
    resultado = eh_letra(caractere)
    print()
    print(f"Resultado retornado: {resultado}")
    print()

def menu():
    while True:
        cabecalho()
        
        print("Menu para acesso às 15 Questões da Lista 04 (Funções)".center(60))
        print("=" * 60)
        print()
        
        for i in range(1, 16):
            print(f"{i}. Questão {i}")
            
        print("0. Sair")
        print()
        
        escolha = ler_numero_inteiro("Por favor, escolha uma opção (1-15) ou 0 para sair: ")
        
        if escolha == 0:
            print()
            print("Obrigado por usar! Até breve.")
            print()
            break
            
        elif 1 <= escolha <= 15:
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