#see how i can imlement GUi and get things moving :D
import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.set_caption("Snake")
game_over=False
while not game_over:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()