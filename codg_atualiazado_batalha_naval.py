import random

def criar_tabuleiro(tamanho=5):
    """Cria um tabuleiro vazio com emojis de onda"""
    return [["🌊" for _ in range(tamanho)] for _ in range(tamanho)]

def mostrar_tabuleiro(tabuleiro, mostrar_navios=False):
    """Exibe o tabuleiro na tela com emojis"""
    print("\n   " + " ".join(str(i).rjust(2) for i in range(len(tabuleiro))))
    for i, linha in enumerate(tabuleiro):
        print(str(i).rjust(2), end=" ")
        for celula in linha:
            if celula == "🚢" and not mostrar_navios:
                print("🌊", end=" ")
            else:
                print(celula, end=" ")
        print()

def posicionar_navios(tabuleiro, quantidade=3):
    """Coloca navios aleatórios no tabuleiro"""
    tamanho = len(tabuleiro)
    navios_posicionados = 0
    while navios_posicionados < quantidade:
        x = random.randint(0, tamanho - 1)
        y = random.randint(0, tamanho - 1)
        if tabuleiro[x][y] != "🚢":
            tabuleiro[x][y] = "🚢"
            navios_posicionados += 1

def jogar():
    """Função principal do jogo"""
    while True:
        tamanho_tabuleiro = 5
        tabuleiro = criar_tabuleiro(tamanho_tabuleiro)
        posicionar_navios(tabuleiro)
        
        tentativas = 0
        acertos = 0
        max_tentativas = 10
        
        print("\n=== BATALHA NAVAL ===")
        print(f"Você tem {max_tentativas} tentativas para afundar 3 navios!")
        
        while tentativas < max_tentativas and acertos < 3:
            print(f"\nTentativa {tentativas + 1} de {max_tentativas}")
            print(f"Navios afundados: {acertos}/3")
            mostrar_tabuleiro(tabuleiro)
            
            try:
                x = int(input("Digite a linha (0-4): "))
                y = int(input("Digite a coluna (0-4): "))
                
                if x < 0 or x >= tamanho_tabuleiro or y < 0 or y >= tamanho_tabuleiro:
                    print("Coordenadas inválidas! Use valores entre 0 e 4.")
                    continue
                    
                if tabuleiro[x][y] in ["💥", "🔥"]:
                    print("Você já atirou aqui!")
                    continue
                    
                if tabuleiro[x][y] == "🚢":
                    print("\n💥 BOOM! Você acertou um navio! 💥")
                    tabuleiro[x][y] = "🔥"
                    acertos += 1
                else:
                    print("\n💣 Splash! Tiro na água! 💣")
                    tabuleiro[x][y] = "💥"
                    
                tentativas += 1
                
            except ValueError:
                print("Por favor, digite números válidos!")
        
        # Fim do jogo
        print("\n=== FIM DO JOGO ===")
        mostrar_tabuleiro(tabuleiro, mostrar_navios=True)
        
        if acertos == 3:
            print(f"\n🎉 Parabéns! Você afundou todos os navios em {tentativas} tentativas! 🎉")
        else:
            print("\n😢 Você não conseguiu afundar todos os navios a tempo. 😢")
        
        # Pergunta se quer jogar novamente
        while True:
            resposta = input("\nDeseja jogar novamente? (s/n): ").lower()
            if resposta in ['s', 'n']:
                break
            print("Por favor, digite 's' para sim ou 'n' para não.")
        
        if resposta == 'n':
            print("\nObrigado por jogar! Até a próxima! 👋")
            break

if __name__ == "__main__":
    jogar() 

