import pygame
rect = []
mshgol = []
i = 5
are = True
for x in range(8):
    if x == 0:
        i += 2
    elif x == 2:
        i -= 3
    elif x == 5  or x == 7 or x == 4 or x == 1:
        i -= 1
    elif x == 6:
        i -= 2
    ii = 7
    for n in range(8):
        if n == 2:
            ii -= 3
        elif n == 4:
            ii -= 2
        elif n == 6:
            ii -= 3
        elif n == 7:
            ii -= 1
        rect.append((ii, i))
        ii += 60
    i += 60


def get_pos(pos):
    for l in rect:
        if pos[0] in range(l[0], l[0] +  60, 1) and pos[1] in range(l[1], l[1] + 60, 1):
            return (l[0]//59, l[1]//59)

def get_rect(pos):
    for l in rect:
        if pos[0] in range(l[0], l[0] +  60, 1) and pos[1] in range(l[1], l[1] + 60, 1):
            return l

class Dot:
    def __init__(self, rec, win):
        r = rect[rec][0] + 27
        c = rect[rec][1] + 27
        pygame.draw.circle(win, (255,165,0), (r, c), 10, 30)


class askry:
    def __init__(self, color, rec, win):
        self.rec = rec
        self.win = win
        self.color = color
        if color == "w":
            img = pygame.image.load("./img/white_pawn.png")
        elif color == "b":
            img = pygame.image.load("./img/black_pawn.png")
        self.askry = pygame.transform.scale(img, (55, 55))
    def draw(self):
        self.win.blit(self.askry, rect[self.rec])
        if self.color == "w":
            mshgol.append([self.rec, "askry_w"])
        elif self.color == "b":
            mshgol.append([self.rec, "askry_b"])




class tbyh:
    def __init__(self, color, rec, win):
        self.rec = rec
        self.win = win
        self.color = color
        if color == "w":
            img = pygame.image.load("./img/white_rook.png")
        elif color == "b":
            img = pygame.image.load("./img/black_rook.png")
        self.tbyh = pygame.transform.scale(img, (55, 55))
    def draw(self):
        self.win.blit(self.tbyh, rect[self.rec])
        if self.color == "w":
            mshgol.append([self.rec, "tbyh_w"])
        elif self.color == "b":
            mshgol.append([self.rec, "tbyh_b"])


class hsan:
    def __init__(self, color, rec, win):
        self.rec = rec
        self.win = win
        self.color = color
        if color == "w":
            img = pygame.image.load("./img/white_knight.png")
        elif color == "b":
            img = pygame.image.load("./img/black_knight.png")
        self.hsan = pygame.transform.scale(img, (55, 55))
    def draw(self):
        self.win.blit(self.hsan, rect[self.rec])
        if self.color == "w":
            mshgol.append([self.rec, "hsan_w"])
        elif self.color == "b":
            mshgol.append([self.rec, "hsan_b"])


class fel:
    def __init__(self, color, rec, win):
        self.rec = rec
        self.win = win
        self.color = color
        if color == "w":
            img = pygame.image.load("./img/white_bishop.png")
        elif color == "b":
            img = pygame.image.load("./img/black_bishop.png")
        self.fel = pygame.transform.scale(img, (55, 55))
    def draw(self):
        self.win.blit(self.fel, rect[self.rec])
        if self.color == "w":
            mshgol.append([self.rec, "fel_w"])
        elif self.color == "b":
            mshgol.append([self.rec, "fel_b"])


class wzer:
    def __init__(self, color, rec, win):
        self.rec = rec
        self.win = win
        self.color = color
        if color == "w":
            img = pygame.image.load("./img/white_queen.png")
        elif color == "b":
            img = pygame.image.load("./img/black_queen.png")
        self.wzer = pygame.transform.scale(img, (55, 55))
    def draw(self):
        self.win.blit(self.wzer, rect[self.rec])
        if self.color == "w":
            mshgol.append([self.rec, "wzer_w"])
        elif self.color == "b":
            mshgol.append([self.rec, "wzer_b"])

class mlk:
    def __init__(self, color, rec, win):
        self.rec = rec
        self.win = win
        self.color = color
        if color == "w":
            img = pygame.image.load("./img/white_king.png")
        elif color == "b":
            img = pygame.image.load("./img/black_king.png")
        self.mlk = pygame.transform.scale(img, (55, 55))
    def draw(self):
        self.win.blit(self.mlk, rect[self.rec])
        if self.color == "w":
            mshgol.append([self.rec, "mlk_w"])
        elif self.color == "b":
            mshgol.append([self.rec, "mlk_b"])


if __name__ == "__main__":
    import main
    main.main()
