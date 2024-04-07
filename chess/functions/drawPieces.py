from extra.consts import IMAGES,SQ_SIZE
import pygame as p

def drawPieces(screen,board):
    for row in range(8):
        for col in range(8):
            piece=board[row][col]
            if piece!="--":
                screen.blit(IMAGES[piece],p.Rect(col*SQ_SIZE,row*SQ_SIZE,SQ_SIZE,SQ_SIZE))