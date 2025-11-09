import pygame

pygame.init()
w = 640
h = 480
screen = pygame.display.set_mode((w, h))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # left click
                print("Left Click")
            if event.button == 2:
                # middle click (clicking the scroll wheel)
                print("Middle Click")
            if event.button == 3:
                # right click
                print("Right Click")
            x, y = event.pos
            print(f"{x}, {y}")