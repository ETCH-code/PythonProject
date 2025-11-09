import pygame
pygame.init()

# screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click to Remove Rectangles")

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# create list of white rects
rects = []
for i in range(5):
    rect = pygame.Rect(50 + i * 100, 150, 50, 50)
    rects.append(rect)

running = True
while running:
    screen.fill(BLACK)

    # draw white rects
    for r in rects:
        pygame.draw.rect(screen, WHITE, r)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse = pygame.Rect(pos[0], pos[1], 1, 1)
            idx = mouse.collidelist(rect_list)
            if idx != -1:
                pygame.draw.rect(screen, (0, 0, 0), rect_list[idx])
                pygame.display.flip()

pygame.quit()