import pygame

image = "Images/selected.png"


class Highlight(pygame.sprite.Sprite):
    Instances = []

    def __init__(self):
        super(Highlight, self).__init__()
        self.Instances.append(self)
        self.surf = pygame.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect()

    def Update_Coord(self, coord):
        x, y = coord
        self.rect.topleft = x * 100, y * 100
