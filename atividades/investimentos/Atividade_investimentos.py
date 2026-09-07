def cabecalho():
    print("*" * 60)
    print("Faculdade Estadual Piauí Instituto de Tecnologia - PIT".center(60))
    print("Bacharelado em Inteligência Artificial".center(60))
    print("Disciplina: Algoritmos e Estruturas de Dados I".center(60))
    print("Prof. João Vagner".center(60))
    print("Aluno: Breno Igo B. P. de Araújo".center(60))
    print("*" * 60)
    print()
    print("ATIVIDADE: Leitura, Interpretação e Melhoria de Código".center(60))
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

def formatar_moeda(valor):
    return f"{valor:,.2f}".translate(str.maketrans(",.", ".,"))

def calcular_quanto_investir():
    print()
    print("--- Divisão Ideal do Salário (Regra 50/30/20) ---")
    print()
    
    salario = ler_numero_float("Digite seu salario: R$ ")
    
    essenciais = salario * 0.50
    lazer = salario * 0.20
    investimento = salario * 0.30
    
    print()
    print(f"Essenciais (50%): R$ {formatar_moeda(essenciais)}")
    print(f"Lazer (20%): R$ {formatar_moeda(lazer)}")
    print(f"Investimento (30%): R$ {formatar_moeda(investimento)}")
    print()

def entrada_de_dados():
    print()
    print("--- Simulação de Investimentos ---")
    print()
    
    aporte_inicial = ler_numero_float("Digite seu aporte inicial (R$): ")
    aporte_mensal = ler_numero_float("Digite seu aporte mensal (R$): ")
    taxa_anual = ler_numero_float("Digite sua taxa anual (%): ") / 100
    
    taxa_mensal = ((1 + taxa_anual) ** (1 / 12)) - 1
    
    anos = ler_numero_inteiro("Quantos anos deseja investir: ")
    meses = anos * 12
    
    return aporte_inicial, aporte_mensal, taxa_mensal, meses

def calcular_juros_mensais(aporte_inicial=0.0, mes=0, taxa_mensal=0.0, aporte_mensal=0.0):
    juros = aporte_inicial
    total_investido = aporte_inicial
    
    print()
    print("--- Acompanhamento Anual do Investimento ---")
    print()
    
    for meses in range(1, mes + 1):
        juros = juros * (1 + taxa_mensal)
        juros = juros + aporte_mensal
        total_investido = total_investido + aporte_mensal
        apresentar_juros_mensais(meses, juros)
        
    return total_investido, juros

def apresentar_juros_mensais(meses=0, juros=0.0):
    if meses % 12 == 0:
        print(f"Ano {meses // 12}: R$ {formatar_moeda(juros)}")

def apresentar_juros_finais(total_investido=0.0, juros=0.0):
    print()
    print("-" * 40)
    print("RESULTADO FINAL".center(40))
    print("-" * 40)
    print()
    print(f"Total Investido (Aportes): R$ {formatar_moeda(total_investido)}")
    print(f"Montante Final (Com Juros): R$ {formatar_moeda(juros)}")
    
    lucro = juros - total_investido
    print(f"Lucro Obtido: R$ {formatar_moeda(lucro)}")
    print(f"Rende: R$ {formatar_moeda(juros * 0.01)} ao mês (estimativa de 1% a.m.)")
    
    print("-" * 40)
    print()

def investimento():
    aporte_inicial, aporte_mensal, taxa_mensal, mes = entrada_de_dados()
    
    total_investido, juros = calcular_juros_mensais(aporte_inicial, mes, taxa_mensal, aporte_mensal)
    
    apresentar_juros_finais(total_investido, juros)

def menu():
    while True:
        cabecalho()
        
        print("Menu de Opções".center(60))
        print()
        print("1. Calcular Divisão Ideal do Salário")
        print("2. Simular Investimento (Juros Compostos)")
        print("0. Sair")
        print()
        
        escolha = ler_numero_inteiro("Por favor, escolha uma opção: ")
        
        if escolha == 0:
            print()
            print("Obrigado por usar! Até breve.")
            print()
            break
            
        elif escolha == 1:
            calcular_quanto_investir()
            print()
            input("Pressione ENTER para voltar ao menu...")
            print()
            print()
            
        elif escolha == 2:
            investimento()
            print()
            input("Pressione ENTER para voltar ao menu...")
            print()
            print()
            
        else:
            print()
            print("Opção não encontrada. Por favor, tente novamente.")
            print()

if __name__ == "__main__":
    menu()