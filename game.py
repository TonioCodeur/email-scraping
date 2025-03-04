import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen ,(0, 0, 255), (250, 250), 200)
    pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 50))
    pygame.display.update()
    pygame.display.flip()
pygame.quit()