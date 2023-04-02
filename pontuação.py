import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600), 0)
pontos = 50
textoPontuacao = f"Pontos: {pontos}"
imgTexto = fonte.render(textoPontuacao, True, (255, 255, 0))


while True:

    screen.blit(imgTexto, (300, 100))
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()