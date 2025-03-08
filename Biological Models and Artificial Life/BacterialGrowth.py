import time
import pygame
import numpy as np
import random

COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_BACTERIA = (0, 255, 0)

# Define a probabilidade de crescimento (entre 0 e 1)
GROWTH_PROBABILITY = 0.1

def update(screen, cells, size):
    update_cells = np.copy(cells)

    for row, col in np.ndindex(cells.shape):
        if cells[row, col] == 0:  
            # Contar células vivas ao redor
            alive_neighbors = np.sum(cells[max(0, row-1):row+2, max(0, col-1):col+2])

            # Simular crescimento baseado em probabilidade
            if alive_neighbors > 0 and random.random() < GROWTH_PROBABILITY:
                update_cells[row, col] = 1

        # Determinar a cor da célula
        color = COLOR_BACTERIA if update_cells[row, col] == 1 else COLOR_BG
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return update_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    cells = np.zeros((60, 80))
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
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1  
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 10)
            pygame.display.update()

        time.sleep(0.1)

if __name__ == '__main__':
    main()
