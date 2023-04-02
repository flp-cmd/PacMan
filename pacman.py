import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
fonte = pygame.font.SysFont("arial", 24, True, False)


AZUL = (0, 0, 255)
VERMELHO = (255, 0 ,0)
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 1


class Cenario:

    def __init__(self, tamanho, pac):
        self.pacman = pac
        self.pontos = 0
        self.tamanho = tamanho
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def pintar_pontos(self, tela):
        pontos_x = 28 * self.tamanho
        img_pontos = fonte.render(f"Score: {self.pontos}", True, AMARELO)
        tela.blit(img_pontos, (pontos_x + 10, 10))

    def pintarLinha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            metade = self.tamanho // 2
            cor = PRETO
            if coluna == 2:
                cor = AZUL
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, AMARELO, (x + metade, y + metade), 1, 0)
            if coluna == 5:
                pygame.draw.circle(tela, VERMELHO, (x + metade, y + metade), 5, 0)

    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintarLinha(tela, numero_linha, linha)

    def calcularRegras(self):
        col = self.pacman.coluna_intencao
        lin = self.pacman.linha_intencao
        if 0 <= col < 28 and 0 <= lin < 29:
            if self.matriz[lin][col] != 2:
                self.pacman.aceitar_movimento()
                if self.matriz[lin][col] == 1:
                    self.pontos += 1
                    self.matriz[lin][col] = 0
                elif self.matriz[lin][col] == 5:
                    self.matriz[lin][col] = 0


class Pacman:
    def __init__(self, tamanho):
        self.coluna = 1
        self.linha = 14
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.raio = self.tamanho // 2
        self.vel_x = 0
        self.vel_y = 0
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha

    def calcularRegras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    def pintar(self, tela, aponta):
        match aponta:
            case 1:
                self.pintarCima(tela)
            case 2:
                self.pintarDireita(tela)
            case 3:
                self.pintarBaixo(tela)
            case 4:
                self.pintarEsquerda(tela)
            case _:
                self.pintarDireita(tela)

    def pintarDireita(self, tela):
        # Desenhando o corpo do PacMan
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)
        # Desenhando a boca do PacMan
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio * 0.9, self.centro_y - self.raio * 0.9)
        labio_inferior = (self.centro_x + self.raio * 0.9, self.centro_y + self.raio * 0.9)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)
        # Desenhando o olho
        olho_x = self.centro_x
        olho_y = int(self.centro_y - (self.raio / 2))
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def pintarEsquerda(self, tela):
        # Desenhando o corpo do PacMan
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)
        # Desenhando a boca do PacMan
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x - self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x - self.raio, self.centro_y + self.raio)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)
        # Desenhando o olho
        olho_x = self.centro_x
        olho_y = int(self.centro_y - (self.raio / 2))
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def pintarCima(self, tela):
        # Desenhando o corpo do PacMan
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)
        # Desenhando a boca do PacMan
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x - self.raio, self.centro_y - self.raio)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)
        # Desenhando o olho
        olho_x = self.centro_x + self.raio / 2
        olho_y = self.centro_y
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def pintarBaixo(self, tela):
        # Desenhando o corpo do PacMan
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)
        # Desenhando a boca do PacMan
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y + self.raio)
        labio_inferior = (self.centro_x - self.raio, self.centro_y + self.raio)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)
        # Desenhando o olho
        olho_x = self.centro_x + self.raio / 2
        olho_y = self.centro_y
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def processandoEventos(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                    self.vel_y = 0
                elif event.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE
                    self.vel_y = 0
                elif event.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE
                    self.vel_x = 0
                elif event.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE
                    self.vel_x = 0
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.vel_x = 0
                if event.key == pygame.K_LEFT:
                    self.vel_x = 0
                if event.key == pygame.K_UP:
                    self.vel_y = 0
                if event.key == pygame.K_DOWN:
                    self.vel_y = 0

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao


if __name__ == "__main__":
    size = 600 // 30
    pacman = Pacman(size)
    cenario = Cenario(size, pacman)
    apontando = 2

    while True:
        eventos = pygame.event.get()
        # Calcular as regras:
        pacman.calcularRegras()  # Movendo o pacman
        cenario.calcularRegras()  # Verificando se o movimento é possível
        # Pintar a tela:
        screen.fill(PRETO)  # Removendo rastros de terreno
        cenario.pintar(screen)  # Pintando o cenário atualizado
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    apontando = 2
                elif e.key == pygame.K_LEFT:
                    apontando = 4
                elif e.key == pygame.K_UP:
                    apontando = 1
                elif e.key == pygame.K_DOWN:
                    apontando = 3
        pacman.pintar(screen, apontando)

        cenario.pintar_pontos(screen)  # Escrevendo os pontos no cantow
        pygame.display.update()  # Atualizando o jogo
        pygame.time.delay(125)
        # Processando eventos:
        pacman.processandoEventos(eventos)