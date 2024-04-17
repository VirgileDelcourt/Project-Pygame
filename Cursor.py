import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN


class Cursor(pygame.sprite.Sprite):
    Instance = None
    max_coord = [0, 0]
    selected = None

    def __init__(self, image, max_coord):
        super(Cursor, self).__init__()
        self.surf = pygame.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect()

        self.coord = [0, 0]
        Cursor.max_coord = max_coord
        Cursor.selected = None
        Cursor.Instance = self

    def Update(self, keys):
        self.Move(keys)
        self.rect.topleft = self.coord[0] * 100, self.coord[1] * 100

    def Move(self, keys):
        if keys[K_LEFT]:
            self.coord[0] += -1
        if keys[K_RIGHT]:
            self.coord[0] += 1
        if keys[K_UP]:
            self.coord[1] += -1
        if keys[K_DOWN]:
            self.coord[1] += 1
        self.Check_Coord()

    def Check_Coord(self):
        if self.coord[0] > Cursor.max_coord[0]:
            self.coord[0] = Cursor.max_coord[0]
        if self.coord[0] < 0:
            self.coord[0] = 0
        if self.coord[1] > Cursor.max_coord[1]:
            self.coord[1] = Cursor.max_coord[1]
        if self.coord[1] < 0:
            self.coord[1] = 0
        return self.coord

    def Select(self):
        print("selecting coord " + str(self.coord) + "...")
        Cursor.selected = tuple(self.coord)
        print("selected coords are now : " + str(Cursor.selected))
        return self.selected

    def Clear_Select(self):
        temp = self.selected
        self.selected = None
        return temp
