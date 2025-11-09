import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 400))
screen.fill((200, 200, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    input("Write a sentence: ")
    text = font.render("Hello World!", True, (255, 255, 255), (65, 60, 35))