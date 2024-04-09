from extra.consts import FRAMES_PER_SQPCANIMATION,BRD_LIGHT_COLOR,BRD_DARK_COLOR,SQ_SIZE,IMAGES
import pygame as p
from .drawBoard import drawBoard
from .drawPieces import drawPieces

def animateMove(move,screen,gs,clock):
    dRow=move.edRow-move.stRow
    dCol=move.edCol-move.stCol
    frameCount=(abs(dRow)+abs(dCol))*FRAMES_PER_SQPCANIMATION
    for frame in range(frameCount+1):
        row,col=(move.stRow+dRow*frame/frameCount,move.stCol+dCol*frame/frameCount)
        drawBoard(screen)
        drawPieces(screen,gs.board)
        color=BRD_LIGHT_COLOR if (move.edRow+move.edCol)%2==0 else BRD_DARK_COLOR
        edSq=p.Rect(move.edCol*SQ_SIZE,move.edRow*SQ_SIZE,SQ_SIZE,SQ_SIZE)
        p.draw.rect(screen,color,edSq)
        if move.pcCaptured!="--":
            screen.blit(IMAGES[move.pcCaptured],edSq)
        screen.blit(IMAGES[move.pcMoved],p.Rect(col*SQ_SIZE,row*SQ_SIZE,SQ_SIZE,SQ_SIZE))
        p.display.flip()
        clock.tick(100)