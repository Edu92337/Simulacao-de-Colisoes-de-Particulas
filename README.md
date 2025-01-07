# Simulação de Colisões de Partículas

Este repositório apresenta uma simulação de colisões entre partículas usando o algoritmo **Leapfrog** para resolver as equações do movimento. A simulação é implementada com a biblioteca **Pygame**, e as partículas interagem entre si por meio de colisões elásticas.

## Funcionalidades
- Movimento das partículas utilizando o algoritmo Leapfrog.
- Tratamento de colisões vetorialmente com ajuste de velocidades e posições.
- Adição de novas partículas ao clicar na tela.

## Como funciona
1. **Algoritmo Leapfrog**:
   - Atualiza as posições e velocidades das partículas usando aceleração e velocidades intermediárias para garantir maior precisão.
   - As colisões e novas trajetórias são recalculadas utilizando álgebra vetorial

2. **Colisões**:
   - Detecta colisões entre partículas com base na distância entre elas.
   - Ajusta as velocidades considerando as leis da conservação de momento e energia para colisões elásticas.
   - Evita sobreposição corrigindo as posições das partículas.

## Controles
- **Mouse**: Clique esquerdo para adicionar novas partículas na tela.
- **Tecla ESC**: Para encerrar a simulação.

## Estrutura do Código
- **Particula**: Classe que representa cada partícula, contendo atributos de posição, velocidade, aceleração, cor e raio.
- **verifica_colisao**: Função que trata as colisões entre duas partículas, ajustando as velocidades e posições.
- **Loop Principal**: Controla o movimento e desenha as partículas na tela, além de detectar eventos do mouse.

## Requisitos
- Python 3.8+
- Pygame 2.0+
- Numpy
- math

