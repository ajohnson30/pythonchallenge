import pygame


# optional
if not pygame.font: print 'Warning, no fonts'
if not pygame.mixer: print 'Warning, no sound'

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Caption')
pygame.mouse.set_visible(0)

screen.fill((0, 0, 0))
pygame.display.flip()

while (pygame.event.wait().type != KEYDOWN): pass

