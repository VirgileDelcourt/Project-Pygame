import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE
from time import sleep

from Cursor import Cursor
from Character import Character
from Highlight import Highlight
from Field import Field

pygame.init()

def Create_Char(field, name, sprite, coords):
    if field.Get(coords) is None:
        field.Insert(Character(name, sprite, coords), coords)
    else:
        raise RuntimeError("tried to create character on an already occupied space")


dimx, dimy = (10, 8)
fps = 120

Character.Instances = []

fenetre = pygame.display.set_mode((dimx * 100, dimy * 100))
field = Field((dimx, dimy))
Cursor("Images/cursor.png", (dimx - 1, dimy - 1))
Create_Char(field, "Gmooba", "Images/Perso.png", (0, 0))
Create_Char(field, "Gloomba", "Images/Perso.png", (5, 2))
Create_Char(field, "Invada", "Images/gay_invader.png", (6, 4))
# field.funny_colors()

try:
    game = True
    while game:
        sleep(1 / fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
            if event.type == KEYDOWN:
                if pygame.key.get_pressed()[K_SPACE]:
                    a, o = Cursor.Instance.coord
                    if Cursor.selected == (a, o) and field.Get((a, o)) is not None:
                        # unselect char
                        Cursor.Instance.Clear_Select()
                        field.Clear_Color()
                    elif not Cursor.selected and field.Get((a, o)) is not None:
                        # select char
                        Cursor.Instance.Select()
                        field.Change_Color("blue", field.Get(Cursor.selected).coord)
                        field.Change_Color("light blue", field.Get(Cursor.selected).Possible_Move(field.Get_Dimensions()))
                    elif Cursor.selected and field.Get(Cursor.selected) is not None:
                        # move char
                        coords = Cursor.selected
                        if field.Get(coords).Check_Move((a, o), field.Get_Dimensions()):
                            field.Swap((a, o), Cursor.selected)
                            Cursor.selected = None
                            field.Clear_Color()
                Cursor.Instance.Update(pygame.key.get_pressed())

        for tile in field.Get_All_Tiles():
            fenetre.blit(tile.surf, tile.rect)
        for char in Character.Instances:
            if char.coord == Cursor.selected:
                print(field.Get(Cursor.Instance.coord))
                if field.Get(Cursor.Instance.coord) is None:
                    char.Update_Rect(Cursor.Instance.coord)
                    fenetre.blit(char.surf, char.rect)
                    char.last = Cursor.Instance.coord
                elif field.Get(Cursor.Instance.coord) is not None:
                    char.Update_Rect(char.last)
                    fenetre.blit(char.surf, char.rect)
                print(char.last)
            else:
                char.Update_Rect()
                fenetre.blit(char.surf, char.rect)
        fenetre.blit(Cursor.Instance.surf, Cursor.Instance.rect)
        pygame.display.update()
        
    pygame.quit()
except:
    pygame.quit()
    raise
