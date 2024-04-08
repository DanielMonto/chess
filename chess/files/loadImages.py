import pygame as p
from extra.consts import IMAGES,SQ_SIZE

def loadImages(gs):
    global IMAGES
    for row in range(8):
        for col in range(8):
            square=gs.board[row][col]
            if square!="--":
                filename=f"assets/{square}.png"
                IMAGES[square]=p.transform.scale(p.image.load(filename),(SQ_SIZE,SQ_SIZE))