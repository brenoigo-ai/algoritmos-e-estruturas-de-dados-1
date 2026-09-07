def cabecalho():
    print("*" * 60)
    print("Faculdade Estadual Piauí Instituto de Tecnologia - PIT". center(60))
    print("Bacharelado em Inteligência Artificial".center(60))
    print("Disciplina: Algoritmos e Estruturas de Dados I".center(60))
    print("Professor: João Vagner".center(60))
    print("Aluno: Breno Igo B. P. de Araújo".center(60))
    print("*" * 60)
    print()
    print("AVALIAÇÃO PRÁTICA - PROGRAMAÇÃO".center(60))
    print("Pesquisa de Intenção de Votos".center(60))
    print()

def ler_opcao(mensagem, opcoes_validas):
    while True:
        try:
            opcao = int(input(mensagem))
            if opcao in opcoes_validas:
                return opcao
            print()
            print(f"Opção inválida. Digite uma das opções válidas: {opcoes_validas}")
            print()
        except ValueError:
            print()
            print("Entrada inválida. Digite um número inteiro.")
            print()

def calcular_porcentagem(votos, total_votos):
    if total_votos == 0:
        return 0
    return (votos / total_votos) * 100

def coletar_dados_pesquisa():
    dados = {
        'votos_cachorro_caramelo': 0, 'votos_canarinho_pistola': 0, 'votos_xaropinho': 0, 'votos_brancos_nulo': 0, 'votos_indecisos': 0,
        'renda_1': 0, 'renda_2': 0, 'renda_3': 0,
        'sexo_masculino': 0, 'sexo_feminino': 0,
        'idade_16_34': 0, 'idade_35_59': 0, 'idade_60_mais': 0,
        'escolaridade_fundamental': 0, 'escolaridade_medio': 0, 'escolaridade_superior': 0,
        'raca_brancos': 0, 'raca_pardos': 0, 'raca_pretos': 0, 'raca_amarelos': 0, 'raca_indigenas': 0,
        'religiao_catolicos': 0, 'religiao_evangelicos': 0, 'religiao_outros': 0,
        'total': 0
    }

    while True:
        print("-" * 60)
        print(f"Entrevista nº {dados['total'] + 1}".center(60))
        print("-" * 60)
        print()

        print("Escolha o candidato em quem você votaria:")
        print()
        print("1 - Cachorro Caramelo 🐕")
        print("2 - Canarinho Pistola 🐥")
        print("3 - Xaropinho 🐭")
        print("0 - Brancos/Nulos")
        print("9 - Indecisos")
        print()

        candidato = ler_opcao("Digite a opção desejada: ", [1, 2, 3, 0, 9])

        if candidato == 1:
            dados['votos_cachorro_caramelo'] += 1
        elif candidato == 2:
            dados['votos_canarinho_pistola'] += 1
        elif candidato == 3:
            dados['votos_xaropinho'] += 1
        elif candidato == 0:
            dados['votos_brancos_nulo'] += 1
        else:
            dados['votos_indecisos'] += 1

        print()
        print("Escolha a sua faixa de renda mensal:")
        print()
        print("1 - Até 2 salários mínimos")
        print("2 - De 2 a 5 salários mínimos")
        print("3 - Mais de 5 salários mínimos")
        print()

        renda = ler_opcao("Digite a opção correspondente a sua renda: ", [1, 2, 3])

        if renda == 1:
            dados['renda_1'] += 1
        elif renda == 2:
            dados['renda_2'] += 1
        else:
            dados['renda_3'] += 1

        print()
        print("Escolha o seu sexo:")
        print()
        print("1 - Masculino")
        print("2 - Feminino")
        print()

        sexo = ler_opcao("Digite a opção correspondente ao seu sexo: ", [1, 2])
        if sexo == 1:
            dados['sexo_masculino'] += 1
        else:
            dados['sexo_feminino'] += 1

        print()
        print("Escolha a sua faixa etária:")
        print()
        print("1 - 16 a 34 anos")
        print("2 - 35 a 59 anos")
        print("3 - 60 anos ou mais")
        print()

        idade = ler_opcao("Digite a opção correspondente à sua idade: ", [1, 2, 3])

        if idade == 1:
            dados['idade_16_34'] += 1
        elif idade == 2:
            dados['idade_35_59'] += 1
        else:
            dados['idade_60_mais'] += 1

        print()
        print("Escolha a sua escolaridade:")
        print()
        print("1 - Ensino Fundamental")
        print("2 - Ensino Médio")
        print("3 - Ensino Superior")
        print()

        escolaridade = ler_opcao("Digite a opção correspondente à sua escolaridade: ", [1, 2, 3])
        if escolaridade == 1:
            dados['escolaridade_fundamental'] += 1
        elif escolaridade == 2:
            dados['escolaridade_medio'] += 1
        else:
            dados['escolaridade_superior'] += 1

        print()
        print("Escolha a sua raça:")
        print()
        print("1 - Brancos")
        print("2 - Pardos")
        print("3 - Pretos")
        print("4 - Amarelos")
        print("5 - Indígenas")
        print()

        raça = ler_opcao("Digite a opção correspondente à sua raça: ", [1, 2, 3, 4, 5])

        if raça == 1:
            dados['raca_brancos'] += 1
        elif raça == 2:
            dados['raca_pardos'] += 1
        elif raça == 3:
            dados['raca_pretos'] += 1
        elif raça == 4:
            dados['raca_amarelos'] += 1
        else:
            dados['raca_indigenas'] += 1

        print()
        print("Escolha a sua religião:")
        print()
        print("1 - Católicos")
        print("2 - Evangélicos")
        print("3 - Outras religiões/Nenhuma")
        print()

        religiao = ler_opcao("Digite a opção correspondente à sua religião: ", [1, 2, 3])

        if religiao == 1:
            dados['religiao_catolicos'] += 1
        elif religiao == 2:
            dados['religiao_evangelicos'] += 1
        elif religiao == 3:
            dados['religiao_outros'] += 1

        dados['total'] += 1

        print()
        continuar = ler_opcao("Deseja registrar outra pesquisa de votos? (1 - SIM / 0 - NÃO): ", [0, 1])
        print()

        if continuar == 0:
            break

    return dados

def apresentar_resultados(dados):
    t = dados['total']

    print()
    print("===== RESULTADO DA PESQUISA =====")
    print()

    print(f"Candidato Cachorro Caramelo 🐕: {dados['votos_cachorro_caramelo']} votos - {calcular_porcentagem(dados['votos_cachorro_caramelo'], t):.2f}%")
    print(f"Candidato Canarinho Pistola 🐥: {dados['votos_canarinho_pistola']} votos - {calcular_porcentagem(dados['votos_canarinho_pistola'], t):.2f}%")
    print(f"Candidato Xaropinho 🐭: {dados['votos_xaropinho']} votos - {calcular_porcentagem(dados['votos_xaropinho'], t):.2f}%")
    print(f"Indecisos: {dados['votos_indecisos']} votos - {calcular_porcentagem(dados['votos_indecisos'], t):.2f}%")
    print(f"Brancos/Nulos: {dados['votos_brancos_nulo']} votos - {calcular_porcentagem(dados['votos_brancos_nulo'], t):.2f}%")
    print()
    
    print("===== RENDA =====")
    print(f"Até 2 salários mínimos: {calcular_porcentagem(dados['renda_1'], t):.2f}%")
    print(f"2 a 5 salários mínimos: {calcular_porcentagem(dados['renda_2'], t):.2f}%")
    print(f"Mais de 5 salários mínimos: {calcular_porcentagem(dados['renda_3'], t):.2f}%")
    print()
    
    print("===== SEXO =====")
    print(f"Masculino: {calcular_porcentagem(dados['sexo_masculino'], t):.2f}%")
    print(f"Feminino: {calcular_porcentagem(dados['sexo_feminino'], t):.2f}%")
    print()
    
    print("===== IDADE =====")
    print(f"16 a 34 anos: {calcular_porcentagem(dados['idade_16_34'], t):.2f}%")
    print(f"35 a 59 anos: {calcular_porcentagem(dados['idade_35_59'], t):.2f}%")
    print(f"60 ou mais: {calcular_porcentagem(dados['idade_60_mais'], t):.2f}%")
    print()
    
    print("===== ESCOLARIDADE =====")
    print(f"Ensino Fundamental: {calcular_porcentagem(dados['escolaridade_fundamental'], t):.2f}%")
    print(f"Ensino Médio: {calcular_porcentagem(dados['escolaridade_medio'], t):.2f}%")
    print(f"Ensino Superior: {calcular_porcentagem(dados['escolaridade_superior'], t):.2f}%")
    print()
    
    print("===== COR/RAÇA =====")
    print(f"Brancos: {calcular_porcentagem(dados['raca_brancos'], t):.2f}%")
    print(f"Pardos: {calcular_porcentagem(dados['raca_pardos'], t):.2f}%")
    print(f"Pretos: {calcular_porcentagem(dados['raca_pretos'], t):.2f}%")
    print(f"Amarelos: {calcular_porcentagem(dados['raca_amarelos'], t):.2f}%")
    print(f"Indígenas: {calcular_porcentagem(dados['raca_indigenas'], t):.2f}%")
    print()
    
    print("===== RELIGIÃO =====")
    print(f"Católicos: {calcular_porcentagem(dados['religiao_catolicos'], t):.2f}%")
    print(f"Evangélicos: {calcular_porcentagem(dados['religiao_evangelicos'], t):.2f}%")
    print(f"Outras religiões/nenhuma religião: {calcular_porcentagem(dados['religiao_outros'], t):.2f}%")
    print()

    print("===== CLASSIFICAÇÃO DA ELEIÇÃO =====")

    votos_validos = dados['votos_cachorro_caramelo'] + dados['votos_canarinho_pistola'] + dados['votos_xaropinho']

    if votos_validos > 0:
        perc_valido_caramelo = calcular_porcentagem(dados['votos_cachorro_caramelo'], votos_validos)
        perc_valido_canarinho = calcular_porcentagem(dados['votos_canarinho_pistola'], votos_validos)
        perc_valido_xaropinho = calcular_porcentagem(dados['votos_xaropinho'], votos_validos)

        maior_perc = max(perc_valido_caramelo, perc_valido_canarinho, perc_valido_xaropinho)

        if maior_perc > 50:
            if maior_perc == perc_valido_caramelo:
                vencedor = "Candidato Cachorro Caramelo 🐕"
            elif maior_perc == perc_valido_canarinho:
                vencedor = "Candidato Canarinho Pistola 🐥"
            else:
                vencedor = "Candidato Xaropinho 🐭"

            print(f"O {vencedor} possui mais de 50% dos votos válidos.")
            print(f"Resultado: vitória do {vencedor} no primeiro turno com {maior_perc:.2f}% dos votos válidos!")
        else:
            print("Nenhum candidato atingiu mais de 50% dos votos válidos")
            print("Poderá haver segundo turno.")

    else:
        print("Na presente pesquisa nenhum dos canditatos registraram votos válidos")
    print()

def menu():
    while  True:
        cabecalho()

        print("Menu Principal".center(60))
        print("=" * 60)
        print()
        print("1. Iniciar Pesquisa Eleitoral")
        print("0. Sair")
        print()

        escolha = ler_opcao("Por favor, escolha uma opção: ", [0, 1])

        if escolha == 0:
            print()
            print("Pesquisa Eleitoral Encerrada. Muito obrigado!")
            print()
            break

        elif escolha == 1:
            print()
            dados_pesquisa = coletar_dados_pesquisa()

            if dados_pesquisa['total'] > 0:
                apresentar_resultados(dados_pesquisa)
            else:
                print("Nenhuma entrevista ainda foi registrada.")
                print()

            input("Pressione ENTER para voltar ao menu...")
            print()
            print()

if __name__ == "__main__":
    menu()        