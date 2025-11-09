import pygame

pygame.init()
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
screen.fill((255, 255, 255))
pygame.display.flip()
i = -1
colors = [(255, 85, 85), (255, 125, 65), (255, 245, 85), (85, 205, 85), (85, 245, 255), (65, 55, 130), (100, 45, 105)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            i += 1
            if i >= len(colors):
                sys.exit()
            screen.fill(colors[i])
            pygame.display.flip()

