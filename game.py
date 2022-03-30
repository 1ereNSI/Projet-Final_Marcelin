import pygame
import pytmx
import pyscroll

class Game:
    
    def __init__(self):


        self.screen = pygame.display.set_mode((800,640))
        pygame.display.set_caption("test")
        
        tmx_data = pytmx.util_pygame.load_pygame('test.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    def run(self):
        
        marche =  True
        

        while marche:
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    marche = False

        pygame.quit()