import pygame
import pices
import chess


pygame.mixer.init()
HIG, WID = 480,480

win = pygame.display.set_mode((HIG, WID))
FPS = 60
pygame.display.set_caption("Chess")
bg = pygame.image.load("./img/board.png")
bg = pygame.transform.scale(bg, (WID, HIG))
op = False
board = chess.Board()
d = True
mshgol = []
turn = "black"
trn = pygame.mixer.Sound("./music/Win10Error.mp3")



def put():
    i = 0
    for vvv in range(127):
        ii = str(board)[vvv]
        if ii != " " and ii != "\n":
            mshgol.clear()
            if ii == "r":
                pices.tbyh("w", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            elif ii == "n":
                pices.hsan("w", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            elif ii == "b":
                pices.fel("w", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            elif ii == "q":
                pices.wzer("w", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            elif ii == "k":
                pices.mlk("w", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            elif ii == "p":
                pices.askry("w", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            elif ii == "P":
                pices.askry("b", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            elif ii == "R":
                pices.tbyh("b", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            elif ii == "N":
                pices.hsan("b", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            elif ii == "B":
                pices.fel("b", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            elif ii == "Q":
                pices.wzer("b", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            elif ii == "K":
                pices.mlk("b", i, win).draw()
                if i not in mshgol:
                    mshgol.append(i)
            i += 1

def converter(tub:tuple):
    gg = tub[0]
    ff = tub[1] + 1
    ss = None
    if ff == 0:
        ss = 9
    elif ff == 1:
        ss = 8
    elif ff == 2:
        ss = 7
    elif ff == 3:
        ss = 6
    elif ff == 4:
        ss = 5
    elif ff == 5:
        ss = 4
    elif ff == 6:
        ss = 3
    elif ff == 7:
        ss = 2
    elif ff == 8:
        ss = 1
    if gg == 0:
        hh = "a"+str(ss)
    elif gg == 1:
        hh = "b"+str(ss)
    elif gg == 2:
        hh = "c"+str(ss)
    elif gg == 3:
        hh = "d"+str(ss)
    elif gg == 4:
        hh = "e"+str(ss)
    elif gg == 5:
        hh = "f"+str(ss)
    elif gg == 6:
        hh = "g"+str(ss)
    elif gg == 7:
        hh = "h"+str(ss)
    return hh



def Move(clk1, clk2):
    squ1 = pices.get_pos(clk1)
    squ2 = pices.get_pos(clk2)
    if squ1 != squ2:
        chess1 = converter(squ1)
        chess2 = converter(squ2)
        piecesa = list(board.legal_moves)
        pieces2 = []
        for piece in piecesa:
            piece3 = str(piece)
            pieces2.append(piece3)
        if f'{chess1}{chess2}' in pieces2:
            return [True, chess1, chess2]
        else:
            return [False]
    else:
        return [False]




def Draw():
    win.blit(bg, (0, 0))
    put()
    pygame.display.set_caption(f"Chess - {turn} Turn")
    pygame.display.update()

def ddd(click_one, color="red"):
    dotpos = pices.get_rect(click_one)
    pygame.draw.rect(win,color,(dotpos[0]-2,dotpos[1]-2,60,60), 2)
    pygame.display.update()
do = False
def main():
    click_one = None
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    try:
                        board.pop()
                    except:
                        trn.play()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if click_one != None:
                    click_tow = pygame.mouse.get_pos()
                    ds = Move(click_one, click_tow)
                    if ds[0]:
                        board.push(chess.Move.from_uci(f'{ds[1]}{ds[2]}'))
                        global turn
                        if turn == "black":
                            turn = "white"
                        elif turn == "white":
                            turn = "black"
                    else:
                        pass
                    click_one = None
                    global do
                    do = False
                elif click_one == None:
                    click_one = pygame.mouse.get_pos()
                    if do:
                        do = False
                    elif not do:
                        do = True
        if do:
            ddd(click_one, "blue")
        Draw()
    pygame.quit()
main()
