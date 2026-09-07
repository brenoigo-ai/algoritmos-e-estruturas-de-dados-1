import random

def cabecalho():
    print("*" * 60)
    print("Faculdade Estadual Piauí Instituto de Tecnologia - PIT".center(60))
    print("Bacharelado em Inteligência Artificial".center(60))
    print("Disciplina: Algoritmos e Estruturas de Dados I".center(60))
    print("Prof. João Vagner".center(60))
    print("Aluno: Breno Igo B. P. de Araújo".center(60))
    print("*" * 60)
    print()
    print("ATIVIDADE 05: Leitura e Interpretação de código".center(60))
    print("Explorando a Caverna do PIT".center(60))
    print()

def ler_numero_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print()
            print("Entrada inválida. Por favor, digite um número inteiro válido.")
            print()

def jogar_dungeon():
    energia = 100
    total_itens = 5
    itens_coletados = 0

    print()
    print(f"Você está na Caverna da PIT e precisa coletar {total_itens} itens para escapar.")
    print(f"Explorar a caverna consome energia a cada passo, total de {energia} energia.")
    print()

    while energia > 0 and itens_coletados < total_itens:
        passos = ler_numero_inteiro("Digite a quantidade de passos que deseja andar (1-20): ")

        if passos < 1:
            print()
            print("Você não pode ficar sem andar ou voltar.")
            print()
            continue

        if passos > 20:
            print()
            print("Você não enxerga longe o suficiente para caminhar.")
            print()
            continue

        energia -= passos
        
        print()
        print(f"Você gastou {passos} passos e agora tem {energia} de energia.")

        if energia <= 0:
            print()
            print("Você morreu de fome.")
            print()
            break

        if random.randint(1, 100) <= 30:
            itens_coletados += 1
            print()
            print(f"Você encontrou um item! Itens coletados: {itens_coletados} de {total_itens}")
            print()
        else:
            print()
            print("Você não encontrou itens desta vez.")
            print()
            
        if itens_coletados == total_itens:
            print()
            print("Parabéns, você encontrou todos os itens e saiu da caverna!")
            print()

def menu():
    while True:
        cabecalho()
        
        print("Menu de Opções".center(60))
        print()
        print("1. Iniciar Jogo: Caverna da PIT")
        print("0. Sair")
        print()
        
        escolha = ler_numero_inteiro("Por favor, escolha uma opção: ")
        
        if escolha == 0:
            print()
            print("Obrigado por jogar! Até breve.")
            print()
            break
            
        elif escolha == 1:
            jogar_dungeon()
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