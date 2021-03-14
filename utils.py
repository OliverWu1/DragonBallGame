import pygame

class playerMovement:
    def __init__(self):
        #Import Goku picture
        self.gokuSurf = pygame.image.load('resources/imagens/player/goku/ss4/power.png').convert_alpha()     
        self.gokuSurf = pygame.transform.scale2x(self.gokuSurf)
        
    
    def gokuRun(self, screen, x, y):
        factor = 2
        #crop out picture from gokuSurf for goku run
        self._gokuRunImg1 = self.gokuSurf.subsurface(6*factor, 1*factor, 34*factor, 67*factor)
        self._gokuRunImg2 = self.gokuSurf.subsurface(51*factor, 1*factor, 38*factor, 67*factor)
        screen.blit(self._gokuRunImg1, (x,y))
        screen.blit(self._gokuRunImg2, (x,y))
        

