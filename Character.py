import pygame


class Character(pygame.sprite.Sprite):
    Instances = []

    def __init__(self, name, sprite, coord):
        super(Character, self).__init__()
        self.name = name
        self.surf = pygame.image.load(sprite).convert_alpha()
        self.rect = self.surf.get_rect()
        self.coord = coord
        self.last = coord

        self.move = 2

        self.Instances.append(self)

    def Update_Rect(self, coord=None):
        if coord == None:
            x, y = self.coord
        else:
            x, y = coord
        self.rect.topleft = x * 100, y * 100

    def Move_To(self, coord):
        self.coord = coord
        print("moved to " + str(coord))

    def Get_Move(self):
        ans = []
        for y in range(-self.move, self.move + 1):
            for x in range(-(self.move - abs(y)), (self.move - abs(y)) + 1):
                if (x, y) != (0, 0):
                    ans.append((x, y))
        return ans

    def Possible_Move(self, dimensions):
        ans = []
        for coord in self.Get_Move():
            temp = self.coord[0] + coord[0], self.coord[1] + coord[1]
            if 0 <= temp[0] <= dimensions[0] and 0 <= temp[1] <= dimensions[1]:
                ans.append(temp)
        return ans

    def Check_Move(self, coord, dimensions):
        if coord in self.Possible_Move(dimensions):
            return True
        else:
            return False
