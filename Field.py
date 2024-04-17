from Tile import Tile
from Character import Character


class Field:
    def __init__(self, dimensions):
        x, y = dimensions
        self.field = [[None] * x for _ in range(y)]
        self.tiles = []
        for _y in range(y):
            self.tiles.append([])
            for _x in range(x):
                self.tiles[-1].append(Tile((_x, _y)))

    def Change_Color(self, color, coords):
        if type(coords) != list:
            coords = [coords]
        for coord in coords:
            self.Get_Tile(coord).Color(color)
        return True

    def Clear_Color(self):
        for row in self.tiles:
            for tile in row:
                tile.Color("white")
        return True

    def Get_Tile(self, coord):
        x, y = coord
        return self.tiles[y][x]

    def Get(self, coord):
        x, y = coord
        return self.field[y][x]

    def Insert(self, char, coord):
        x, y = coord
        if self.Get(coord) is None:
            self.field[y][x] = char
            if issubclass(type(char), Character):
                char.coord = coord
            return True
        return False

    def Remove(self, coord):
        x, y = coord
        if self.Get(coord) is not None:
            ans = self.field[y][x]
            self.field[y][x] = None
            return ans
        return False

    def Swap(self, coords1, coords2):
        print("movin'")
        char1 = self.Get(coords1)
        char2 = self.Get(coords2)
        self.Remove(coords1)
        self.Remove(coords2)
        self.Insert(char1, coords2)
        self.Insert(char2, coords1)
        if issubclass(type(char1), Character):
            print("char1 is character")
            char1.Move_To(coords2)
        if issubclass(type(char2), Character):
            print("char2 is character")
            char2.Move_To(coords1)

    def funny_colors(self):
        a, o = self.Get_Dimensions()
        for y in range(o):
            for x in range(a):
                if (x + y) % 2 == 0:
                    self.Get_Tile((x, y)).Color("green")
                else:
                    self.Get_Tile((x, y)).Color("dark green")

    def Get_Dimensions(self):
        x = len(self.field[0])
        y = len(self.field)
        return x, y

    def Get_All_Tiles(self):
        ans = []
        for row in self.tiles:
            ans.extend(row)
        return ans
