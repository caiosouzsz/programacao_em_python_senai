import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
largura = 600
altura = 400
tamanho_celula = 20

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("🐍 Jogo da Cobrinha")

# Cores
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
branco = (255, 255, 255)

# Fonte
fonte = pygame.font.SysFont("arial", 25)

# Função para mostrar a pontuação
def mostrar_pontuacao(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, branco)
    tela.blit(texto, [10, 10])

# Função principal
def jogo():
    # Posição inicial da cobra
    cobra_pos = [[300, 200], [280, 200], [260, 200]]
    direcao = "DIREITA"

    # Posição inicial da comida
    comida_pos = [random.randrange(0, largura // tamanho_celula) * tamanho_celula,
                  random.randrange(0, altura // tamanho_celula) * tamanho_celula]
    comida_spawn = True

    velocidade = 10
    relogio = pygame.time.Clock()

    while True:
        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != "BAIXO":
                    direcao = "CIMA"
                elif evento.key == pygame.K_DOWN and direcao != "CIMA":
                    direcao = "BAIXO"
                elif evento.key == pygame.K_LEFT and direcao != "DIREITA":
                    direcao = "ESQUERDA"
                elif evento.key == pygame.K_RIGHT and direcao != "ESQUERDA":
                    direcao = "DIREITA"

        # Atualiza a posição da cabeça
        if direcao == "CIMA":
            nova_cabeca = [cobra_pos[0][0], cobra_pos[0][1] - tamanho_celula]
        elif direcao == "BAIXO":
            nova_cabeca = [cobra_pos[0][0], cobra_pos[0][1] + tamanho_celula]
        elif direcao == "ESQUERDA":
            nova_cabeca = [cobra_pos[0][0] - tamanho_celula, cobra_pos[0][1]]
        elif direcao == "DIREITA":
            nova_cabeca = [cobra_pos[0][0] + tamanho_celula, cobra_pos[0][1]]

        # Insere a nova cabeça
        cobra_pos.insert(0, nova_cabeca)

        # Verifica se comeu a comida
        if cobra_pos[0] == comida_pos:
            comida_spawn = False
        else:
            cobra_pos.pop()

        # Cria nova comida
        if not comida_spawn:
            comida_pos = [random.randrange(0, largura // tamanho_celula) * tamanho_celula,
                          random.randrange(0, altura // tamanho_celula) * tamanho_celula]
            comida_spawn = True

        # Verifica colisões
        if (cobra_pos[0][0] < 0 or cobra_pos[0][0] >= largura or
            cobra_pos[0][1] < 0 or cobra_pos[0][1] >= altura):
            break  # Bateu na parede

        for parte in cobra_pos[1:]:
            if cobra_pos[0] == parte:
                break  # Bateu no próprio corpo
        else:
            # Continua o jogo
            tela.fill(preto)

            # Desenha cobra
            for pos in cobra_pos:
                pygame.draw.rect(tela, verde, pygame.Rect(pos[0], pos[1], tamanho_celula, tamanho_celula))

            # Desenha comida
            pygame.draw.rect(tela, vermelho, pygame.Rect(comida_pos[0], comida_pos[1], tamanho_celula, tamanho_celula))

            # Mostra pontuação
            mostrar_pontuacao(len(cobra_pos) - 3)

            # Atualiza tela
            pygame.display.flip()
            relogio.tick(velocidade)
            continue

        break  # Sai do loop se bateu

    # Tela de fim de jogo
    tela.fill(preto)
    msg = fonte.render(f"Game Over! Pontos: {len(cobra_pos) - 3}", True, vermelho)
    tela.blit(msg, [largura // 6, altura // 3])
    pygame.display.flip()
    pygame.time.wait(2000)
    jogo()  # Reinicia o jogo

# Inicia o jogo
jogo()
