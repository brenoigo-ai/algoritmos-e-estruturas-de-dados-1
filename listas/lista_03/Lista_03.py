def cabecalho():
    print("*" * 60)
    print("Faculdade Estadual Piauí Instituto de Tecnologia - PIT".center(60))
    print("Bacharelado em Inteligência Artificial".center(60))
    print("Disciplina: Algoritmos e Estruturas de Dados I".center(60))
    print("Prof. João Vagner".center(60))
    print("Aluno: Breno Igo B. P. de Araújo".center(60))
    print("*" * 60)
    print()
    print("ATIVIDADE 03 - Comandos de repetição".center(60))
    print()

def ler_numero_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(',','.'))
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

def questao_1():
    print()
    print("1. Escrever o nome 10x na tela.")
    print()
    nome = input("Digite seu nome: ")
    print()
    for _ in range(10):
        print(nome)
    print()

def questao_2():
    print()
    print("2. Múltiplos de 5 no intervalo de 1 a 100.")
    print()
    for i in range(1, 101):
        if i % 5 == 0:
            print(i, end=" ")
    print()
    print()

def questao_3():
    print()
    print("3. Imprimir os valores no intervalo de 33 a 3.")
    print()
    for i in range(33, 2, -1):
        print(i, end=" ")
    print()
    print()

def questao_4():
    print()
    print("4. Soma dos trinta primeiros números naturais.")
    print()
    soma = 0
    for i in range(1, 31):
        soma += i
    print(f"A soma é: {soma}")
    print()

def questao_5():
    print()
    print("5. Somatório dos números ímpares no intervalo de 1 até 200.")
    print()
    soma = 0
    for i in range(1, 201):
        if i % 2 != 0:
            soma += i
    print(f"O somatório é: {soma}")
    print()

def questao_6():
    print()
    print("6. Somatório dos valores divisíveis por 3 e 7 de 1 a 900.")
    print()
    soma = 0
    for i in range(1, 901):
        if i % 3 == 0 and i % 7 == 0:
            soma += i
    print(f"O somatório é: {soma}")
    print()

def questao_7():
    print()
    print("7. Quadrado dos números no intervalo fechado de 1 a 20.")
    print()
    for i in range(1, 21):
        print(f"{i}^2 = {i**2}")
    print()

def questao_8():
    print()
    print("8. Somatório de 10 valores numéricos inteiros.")
    print()
    soma = 0
    for i in range(1, 11):
        valor = ler_numero_inteiro(f"Digite o {i}º valor: ")
        soma += valor
    print()
    print(f"O somatório é: {soma}")
    print()

def questao_9():
    print()
    print("9. Imprimir o maior e o menor número de uma lista de 10 números.")
    print()
    maior = float('-inf')
    menor = float('inf')
    for i in range(1, 11):
        valor = ler_numero_inteiro(f"Digite o {i}º número: ")
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    print()
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print()

def questao_10():
    print()
    print("10. Soma e média aritmética dos pares de 40 até 80.")
    print()
    soma = 0
    cont = 0
    for i in range(40, 81):
        if i % 2 == 0:
            soma += i
            cont += 1
    media = soma / cont if cont > 0 else 0
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
    print()

def questao_11():
    print()
    print("11. Tabuada de multiplicar (0 a 10) de um número inteiro positivo.")
    print()
    while True:
        num = ler_numero_inteiro("Digite um número inteiro positivo: ")
        if num > 0:
            break
        print("Por favor, digite apenas números positivos.")
    print()
    for i in range(11):
        print(f"{num} x {i} = {num * i}")
    print()

def questao_12():
    print()
    print("12. Múltiplos de 3 e 5 de 1 a NUM.")
    print()
    num = ler_numero_inteiro("Digite o valor de NUM: ")
    print()
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
    print()
    print()

def questao_13():
    print()
    print("13. Quantidade de pares e ímpares (20 números).")
    print()
    pares = 0
    impares = 0
    for i in range(1, 21):
        valor = ler_numero_inteiro(f"Digite o {i}º número: ")
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1
    print()
    print(f"Quantidade de pares: {pares}")
    print(f"Quantidade de ímpares: {impares}")
    print()

def questao_14():
    print()
    print("14. Quantos números maiores que 30 foram digitados (15 números).")
    print()
    maiores_30 = 0
    for i in range(1, 16):
        valor = ler_numero_float(f"Digite o {i}º número: ")
        if valor > 30:
            maiores_30 += 1
    print()
    print(f"Quantidade de números maiores que 30: {maiores_30}")
    print()

def questao_15():
    print()
    print("15. Soma dos positivos e o total de números negativos (20 números).")
    print()
    soma_positivos = 0
    total_negativos = 0
    for i in range(1, 21):
        valor = ler_numero_float(f"Digite o {i}º número: ")
        if valor > 0:
            soma_positivos += valor
        elif valor < 0:
            total_negativos += 1
    print()
    print(f"Soma dos positivos: {soma_positivos}")
    print(f"Total de negativos: {total_negativos}")
    print()

def questao_16():
    print()
    print("16. Fatorial do número N.")
    print()
    while True:
        n = ler_numero_inteiro("Digite o valor de N: ")
        if n >= 0:
            break
        print("Por favor, digite apenas valores não negativos.")
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print()
    print(f"O fatorial de {n} é: {fatorial}")
    print()

def questao_17():
    print()
    print("17. Naturais no intervalo fechado (inferior a superior).")
    print()
    inf = ler_numero_inteiro("Limite inferior: ")
    sup = ler_numero_inteiro("Limite superior: ")
    print()
    print("Saída: ", end="")
    for i in range(inf, sup + 1):
        print(i, end=" ")
    print()
    print()

def questao_18():
    print()
    print("18. Série de Fibonacci até o N-ésimo termo.")
    print()
    n = ler_numero_inteiro("Digite a quantidade de termos: ")
    print()
    a, b = 1, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
    print()

def questao_19():
    print()
    print("19. Série de RICCI (dois termos fornecidos pelo usuário).")
    print()
    t1 = ler_numero_inteiro("Digite o primeiro termo: ")
    t2 = ler_numero_inteiro("Digite o segundo termo: ")
    n = ler_numero_inteiro("Digite a quantidade de termos: ")
    print()
    a, b = t1, t2
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
    print()

def questao_20():
    print()
    print("20. Série: 1, 4, 4, 2, 5, 5, 3, 6, 6, 4, 7, 7...")
    print()
    n = ler_numero_inteiro("Digite a quantidade de termos N: ")
    print()
    cont = 1
    termos_impressos = 0
    while termos_impressos < n:
        print(cont, end=" ")
        termos_impressos += 1
        if termos_impressos < n:
            print(cont + 3, end=" ")
            termos_impressos += 1
        if termos_impressos < n:
            print(cont + 3, end=" ")
            termos_impressos += 1
        cont += 1
    print()
    print()

def questao_21():
    print()
    print("21. Número H = 1 + 1/2 + 1/3... + 1/N.")
    print()
    n = ler_numero_inteiro("Digite o valor de N: ")
    h = 0
    for i in range(1, n + 1):
        h += 1 / i
    print()
    print(f"O número H é: {h:.4f}")
    print()

def questao_22():
    print()
    print("22. Número S = 1 + 1/2^2 + 1/3^3... + 1/N^N.")
    print()
    n = ler_numero_inteiro("Digite o valor de N: ")
    s = 0
    for i in range(1, n + 1):
        s += 1 / (i ** i)
    print()
    print(f"O número S é: {s:.4f}")
    print()

def questao_23():
    print()
    print("23. Quantidade de pares e ímpares (termina ao digitar NEGATIVO).")
    print()
    pares = 0
    impares = 0
    while True:
        valor = ler_numero_inteiro("Digite um valor inteiro positivo (ou negativo para sair): ")
        if valor < 0:
            break
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1
    print()
    print(f"Quantidade de pares: {pares}")
    print(f"Quantidade de ímpares: {impares}")
    print()

def questao_24():
    print()
    print("24. Menu de operações entre dois números.")
    print()
    n1 = ler_numero_float("Digite o primeiro número: ")
    n2 = ler_numero_float("Digite o segundo número: ")
    print()
    while True:
        print("MENU")
        print("A - Maior Número")
        print("B - Menor Número")
        print("C - Média Aritmética")
        print("D - Finalizar")
        print()
        opcao = input("Escolha uma opção: ").upper()
        
        if opcao == "A":
            print()
            print(f"Maior Número: {max(n1, n2)}")
            print()
        elif opcao == "B":
            print()
            print(f"Menor Número: {min(n1, n2)}")
            print()
        elif opcao == "C":
            print()
            print(f"Média Aritmética: {(n1 + n2) / 2}")
            print()
        elif opcao == "D":
            print()
            print("Operação finalizada.")
            print()
            break
        else:
            print()
            print("Opção inválida.")
            print()

def questao_25():
    print()
    print("25. Somatório dos números negativos (termina com 0).")
    print()
    soma = 0
    while True:
        valor = ler_numero_inteiro("Digite um número inteiro (0 para sair): ")
        if valor == 0:
            break
        if valor < 0:
            soma += valor
    print()
    print(f"Somatório dos negativos: {soma}")
    print()

def questao_26():
    print()
    print("26. Somatório dos números pares (termina com 0).")
    print()
    soma = 0
    while True:
        valor = ler_numero_inteiro("Digite um número inteiro positivo (0 para sair): ")
        if valor == 0:
            break
        if valor > 0 and valor % 2 == 0:
            soma += valor
    print()
    print(f"Somatório dos pares: {soma}")
    print()

def menu():
    while True:
        cabecalho()
        
        print("Menu para acesso às 26 Questões da Lista 03 (Repetição)".center(60))
        print("=" * 60)
        print()
        
        for i in range(1, 27):
            print(f"{i}. Questão {i}")
            
        print("0. Sair")
        print()
        
        escolha = ler_numero_inteiro("Por favor, escolha uma opção (1-26) ou 0 para sair: ")
        
        if escolha == 0:
            print()
            print("Obrigado por usar! Até breve.")
            print()
            break
            
        elif 1 <= escolha <= 26:
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