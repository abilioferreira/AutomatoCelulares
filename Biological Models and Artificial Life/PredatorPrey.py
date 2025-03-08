import time
import pygame
import numpy as np
import random

COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_PREY = (0, 255, 0)
COLOR_PREDATOR = (255, 0, 0)

# Probabilidades e configurações
GROWTH_PROBABILITY = 0.1  # Probabilidade reduzida para limitar crescimento inicial
PREDATION_PROBABILITY = 0.3
PREDATOR_STARVATION_TIME = 5

# Inicialização dos tempos de fome dos predadores
starvation_time = None

def update(screen, cells, size):
    global starvation_time
    update_cells = np.copy(cells)
    starvation_time = np.where(starvation_time > 0, starvation_time - 1, 0)

    for row, col in np.ndindex(cells.shape):
        cell_value = cells[row, col]

        if cell_value == 0:  # Espaço vazio, possível crescimento de presas
            alive_neighbors = np.sum(cells[max(0, row-1):row+2, max(0, col-1):col+2] == 1)
            if alive_neighbors > 0 and random.random() < GROWTH_PROBABILITY:
                update_cells[row, col] = 1

        elif cell_value == 1:  # Presa, possível predação
            predator_neighbors = np.sum(cells[max(0, row-1):row+2, max(0, col-1):col+2] == 2)
            if predator_neighbors > 0 and random.random() < PREDATION_PROBABILITY:
                update_cells[row, col] = 2
                starvation_time[row, col] = PREDATOR_STARVATION_TIME

        elif cell_value == 2:  # Predador, verifica fome
            if starvation_time[row, col] <= 0:
                update_cells[row, col] = 0  # Predador morre de fome

        # Determinar a cor da célula
        color = (
            COLOR_PREY if update_cells[row, col] == 1 else
            COLOR_PREDATOR if update_cells[row, col] == 2 else
            COLOR_BG
        )
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return update_cells

def main():
    global starvation_time

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    cells = np.zeros((60, 80))
    starvation_time = np.zeros_like(cells)

    screen.fill(COLOR_GRID)
    update(screen, cells, 10)
    pygame.display.flip()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Clique único para adicionar presa ou predador
                pos = pygame.mouse.get_pos()
                if event.button == 1:  # Botão esquerdo
                    cells[pos[1] // 10, pos[0] // 10] = 1  # Semear presa
                elif event.button == 3:  # Botão direito
                    cells[pos[1] // 10, pos[0] // 10] = 2  # Semear predador
                    starvation_time[pos[1] // 10, pos[0] // 10] = PREDATOR_STARVATION_TIME
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 10)
            pygame.display.update()

        time.sleep(0.1)

if __name__ == '__main__':
    main()
