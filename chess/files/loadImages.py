import pygame as p
from extra.consts import IMAGES,INITIAL_BOARD,SQ_SIZE

def loadImages():
    global IMAGES
    for row in range(8):
        for col in range(8):
            square=INITIAL_BOARD[row][col]
            if square!="--":
                filename=f"assets/{square}.png"
                IMAGES[square]=p.transform.scale(p.image.load(filename),(SQ_SIZE,SQ_SIZE))