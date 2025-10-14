"""
Algoritmo 331 - Um marciano chegou a uma floresta e se escondeu atrás de uma
das 100 árvore quando viu um caçador. O caçador só tinha cinco balas em sua
espingarda. Cada vez que ele atirava, e não acertava, é claro, o marciano dizia:
estou mais à direita ou mais à esquerda. Se o caçador não conseguir acertar o
marciano, ele será levado para Marte. Implementar este jogo para dois jogadores,
onde um escolhe a árvore em que o marciano irá se esconder, e o outro tenta
acertar.
"""
def escolher_arvore(jogador, arvore_correta):
    """
    Funcao que permite ao jogador escolher a arvore onde o marciano esta escondido.
    Ela recebe o nome e o numero da arvore correta e retorna True se o jogador acertar
    ou False se errar.

    Args:
        jogador (str): Nome do jogador que está tentando adivinhar.
        arvore_correta (int): A árvore onde o marciano está escondido.
    """
    while True:
        arvore = int(input(f"{jogador}, escolha uma árvore entre 1 e 100: "))
        if arvore < 1 or arvore > 100:
            print("Número inválido. Escolha uma árvore entre 1 e 100.")
        elif arvore == arvore_correta:
            print(f"Parabéns {jogador}! Você acertou a árvore {arvore_correta}!")
            return True
        else:
            if arvore < arvore_correta:
                print("O marciano está mais à direita.")
            else:
                print("O marciano está mais à esquerda.")
            return False

def definir_arvore_correta(jogador):
    """
    Funcao onde o jogador escolhe a arvore correta onde o marciano esta escondido.
    Ela recebe o nome do jogador e retorna o numero da arvore correta.  
    """
    while True:
        arvore = int(input(f"{jogador}, escolha uma árvore entre 1 e 100 para esconder o marciano: "))
        if arvore < 1 or arvore > 100:
            print("Número inválido. Escolha uma árvore entre 1 e 100.")
        else:
            return arvore

def jogo():
    import os

    """
    Função principal do jogo.

    Args:
        jogador (str): Nome do jogador que está tentando adivinhar.
        arvore_correta (int): A árvore onde o marciano está escondido.
    """
    print("Bem-vindo ao jogo do marciano!")
    print("O primeiro jogador escolhe a árvore onde o marciano está escondido.")
    jogador_marciano = input("Digite o nome do primeiro jogador: ")   
    arvore_correta = definir_arvore_correta(jogador_marciano)
    # Limpa a tela para o segundo jogador
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # O cacador so tem 5 balas, portanto, 5 tentativas
    print("Agora é a vez do segundo jogador tentar acertar a árvore onde o marciano está escondido.")
    jogador_cacador = input("Digite o nome do segundo jogador: ")
    tentativas = 5
    print(f"\n{jogador_cacador}, você tera {tentativas} para acerta o marciano.")
    
    for tentativa in range(1, tentativas + 1):
        print(f"\nTentativa {tentativa} de {tentativas}")
        if escolher_arvore(jogador_cacador, arvore_correta):
            break
    else:
        print(f"Que pena! {jogador_cacador}, você não conseguiu acertar. O marciano estava na árvore {arvore_correta}.")
        print(f"{jogador_marciano} vence e leva o marciano para Marte!")

if __name__ == "__main__":
    jogo()