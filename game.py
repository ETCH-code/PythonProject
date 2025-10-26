import sys
import pygame

resolution = (800, 450)
color = (255, 187, 0)
screen = pygame.display.set_mode(resolution)

while True:
    screen.fill(color)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()