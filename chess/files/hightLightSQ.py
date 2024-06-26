import pygame as p
from extra.consts import SQ_SIZE,SQ_SELECTED_COLOR,SQ_SELECTED_MOVES_COLOR,LAST_MOVE_COLOR

def hightLightSQ(screen,gs,vms,sqSelected):
    if len(gs.moveLog)>0:
        surf=p.Surface((SQ_SIZE,SQ_SIZE))
        surf.set_alpha(100)
        surf.fill(p.Color(LAST_MOVE_COLOR))
        screen.blit(surf,(SQ_SIZE*gs.moveLog[-1].edCol,SQ_SIZE*gs.moveLog[-1].edRow))
        screen.blit(surf,(SQ_SIZE*gs.moveLog[-1].stCol,SQ_SIZE*gs.moveLog[-1].stRow))
    if sqSelected!=():
        row,col=sqSelected
        if gs.board[row][col][0]=="w" if gs.whiteToMove else "b":
            surf=p.Surface((SQ_SIZE,SQ_SIZE))
            surf.set_alpha(100)
            surf.fill(p.Color(SQ_SELECTED_COLOR))
            screen.blit(surf,(SQ_SIZE*col,SQ_SIZE*row))
            surf.fill(p.Color(SQ_SELECTED_MOVES_COLOR))
            for mv in vms:
                if mv.stRow==row and mv.stCol==col:
                    screen.blit(surf,(SQ_SIZE*mv.edCol,SQ_SIZE*mv.edRow))