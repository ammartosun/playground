import pygame

screen = pygame.display.set_mode([800,600])

color = [0,94,0]

screen.fill(color)

pygame.draw.line(screen,[111,79,29],[0,0],[400,300])

pygame.draw.rect(screen,[0,0,0],[10,20,200,100])


pygame.display.flip()

exitFlag = False

while not exitFlag:
       event = pygame.event.poll()
       if event.type==pygame.QUIT:
          exitFlag = True