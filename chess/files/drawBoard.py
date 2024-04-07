import pygame as p
from extra.consts import SQ_SIZE,BRD_LIGHT_COLOR,BRD_DARK_COLOR

def drawBoard(screen):
    colors=p.Color(BRD_LIGHT_COLOR),p.Color(BRD_DARK_COLOR)
    for row in range(8):
        for col in range(8):
            color=colors[(col+row)%2]
            p.draw.rect(screen,color,p.Rect(col*SQ_SIZE,row*SQ_SIZE,SQ_SIZE,SQ_SIZE))