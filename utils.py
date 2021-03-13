import pygame

class playerMovement:
    def __init__(self):
        #Import Goku picture
        self.gokuSurf = pygame.image.load('resources/imagens/player/goku/ss4/power.png')
    
    def gokuRun(self, screen, x, y):
        #crop out picture from gokuSurf for goku run
        self._gokuRunImg1 = self.gokuSurf.subsurface(6, 1, 34, 67).convert_alpha()
        self._gokuRunImg2 = self.gokuSurf.subsurface(51, 1, 38, 67).convert_alpha()
        screen.blit(self._gokuRunImg1, (x,y))
        pygame.display.update()
        screen.blit(self._gokuRunImg2, (x,y))
        pygame.display.update()
        

