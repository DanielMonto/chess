import pygame as p
from extra.consts import WIDTH,HEIGHT

def drawText(screen,text):
    font=p.font.SysFont("Helvica",32,italic=True)
    textObj=font.render(text,0,p.Color("#0000ff"))
    textLoc=p.Rect(0,0,WIDTH,HEIGHT).move(WIDTH/2 - textObj.get_width()/2,HEIGHT/2 - textObj.get_height()/2)
    screen.blit(textObj,textLoc)
    textObj=font.render(text,0,p.Color("#00ffff"))
    screen.blit(textObj,textLoc.move(2,2))