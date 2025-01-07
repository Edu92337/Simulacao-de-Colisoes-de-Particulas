import pygame
import numpy as np
import math 


#SETUP
simulacao_ativa = True
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simulação")
clock = pygame.time.Clock()
running = True
dt = 1/60
w,h = screen.get_width()//2,screen.get_height()//2


class Particula:
    def __init__(self):
        self.cores = ['black','blue','orange','purple','yellow','green']
        self.posicao = pygame.Vector2(np.random.randint(screen.get_width() // 3, 2 * screen.get_width() // 3))
        self.velocidade =  pygame.Vector2(np.random.randint(-10,10),np.random.randint(-10,10))
        self.aceleracao =  pygame.Vector2(0,10)
        self.raio = 10
        self.trajetoria = [self.posicao]
        self.cor = self.cores[np.random.randint(0,6)]
        
    def draw(self):
        return pygame.draw.circle(screen, self.cor, self.posicao, self.raio)

    def movimento(self):
        v_meio_passo = self.velocidade + self.aceleracao*dt/2
        self.posicao = self.posicao + v_meio_passo*dt
        self.velocidade = v_meio_passo + self.aceleracao*dt/2

        if self.posicao.y +self.raio >= screen.get_height():
            self.velocidade.y = - self.velocidade.y
        if self.posicao.x -self.raio <= 0 or self.posicao.x + self.raio >= screen.get_width():
            self.velocidade.x = -self.velocidade.x
        #Eixo x
        if self.posicao.x < self.raio:
            ajuste = self.raio - self.posicao.x
            self.posicao.x += ajuste
        elif self.posicao.x > screen.get_width() - self.raio:
            ajuste = self.posicao.x - (screen.get_width() - self.raio)
            self.posicao.x -= ajuste
        # Eixo y
        if self.posicao.y > screen.get_height() - self.raio:
            ajuste = self.posicao.y - (screen.get_height() - self.raio)
            self.posicao.y -= ajuste

        
        self.trajetoria.append(self.posicao.xy[:])

    
#FUNÇÕES DA SIMULAÇÃO 
def verifica_colisao(p1, p2, coef_rest=1.0):
    distancia = math.dist(p1.posicao, p2.posicao)
    if distancia <= (p1.raio + p2.raio):
        normal = (p1.posicao - p2.posicao).normalize()
        tangencial = pygame.Vector2(-normal.y, normal.x)

        v1n = normal.dot(p1.velocidade)
        v1t = tangencial.dot(p1.velocidade)
        v2n = normal.dot(p2.velocidade)
        v2t = tangencial.dot(p2.velocidade)

        
        m1, m2 = 1, 1  
        v1n_nova = (v1n * (m1 - m2) + 2 * m2 * v2n) / (m1 + m2) * coef_rest
        v2n_nova = (v2n * (m2 - m1) + 2 * m1 * v1n) / (m1 + m2) * coef_rest

        
        p1.velocidade = tangencial * v1t + normal * v1n_nova
        p2.velocidade = tangencial * v2t + normal * v2n_nova

        # Reajuste de posições
        ajuste = (p1.raio + p2.raio - distancia) / 2
        p1.posicao += normal * ajuste
        p2.posicao -= normal * ajuste


#SIMULAÇÃO
n = np.random.randint(1,21)
particulas =[]
for _ in range(n):
    p = Particula()
    particulas.append(p)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:# nao está identificando as colisões
                if event.button == 1:
                    p = Particula()  
                    particulas.append(p)
    
    if simulacao_ativa:
        screen.fill("white")
            
        for particula in particulas:
            particula.draw()
            particula.movimento()
        for i in range(len(particulas)):
            for j in range(i+1,len(particulas)):
                verifica_colisao(particulas[i],particulas[j])


    
        pygame.display.flip()
        dt = clock.tick(60) / 100

pygame.quit()