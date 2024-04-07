import pygame as p
from extra.consts import SQ_SIZE

def drawBoard(screen):
    colors=p.Color("white"),p.Color("gray")
    for row in range(8):
        for col in range(8):
            color=colors[(col+row)%2]
            p.draw.rect(screen,color,p.Rect(col*SQ_SIZE,row*SQ_SIZE,SQ_SIZE,SQ_SIZE))