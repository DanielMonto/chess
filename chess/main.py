import pygame as p
from files.gameState import GameState
from files.move import Move
from files.hightLightSQ import hightLightSQ
from extra.consts import WIDTH,HEIGHT,MAX_FPS,SQ_SIZE,WHITE_PIECES,BLACK_PIECES
from files.loadImages import loadImages
from files.drawBoard import drawBoard
from files.drawPieces import drawPieces

def main():
    p.init()
    screen=p.display.set_mode((WIDTH,HEIGHT))
    clock=p.time.Clock()
    gs=GameState()
    validMoves=gs.getValidMoves()
    vmMade=False
    loadImages()
    running=True
    sqSelected=()
    playerClicks=[]
    while running:
        drawBoard(screen)
        hightLightSQ(screen,gs,validMoves,sqSelected)
        drawPieces(screen,gs.board)
        for e in p.event.get():
            if e.type==p.QUIT:
                running=False
            elif e.type==p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    sqSelected=()
                    playerClicks=[]
                    vmMade=True
            elif e.type==p.MOUSEBUTTONDOWN:
                location=p.mouse.get_pos()
                col=location[0]//SQ_SIZE
                row=location[1]//SQ_SIZE
                if sqSelected==(row,col):
                    playerClicks=[sqSelected]
                else:
                    sqSelected=(row,col)
                    if (len(playerClicks)==1 and gs.whiteToMove and gs.board[row][col][0]=="w") or (len(playerClicks)==1 and gs.board[row][col][0]=="b" and not gs.whiteToMove):
                        playerClicks=[sqSelected]
                    if (gs.board[row][col]=="--" and len(playerClicks)==0) or (gs.board[row][col][0]=="b" and gs.whiteToMove and len(playerClicks)==0) or (gs.board[row][col][0]=="w" and len(playerClicks)==0 and not gs.whiteToMove):
                        sqSelected=()
                        playerClicks=[]
                        continue
                    else:
                        playerClicks.append(sqSelected)
                if len(playerClicks)==2:
                    move=Move(playerClicks[0],playerClicks[1],gs.board)
                    if move.pcMoved[1]=="K" and abs(move.edCol-move.stCol)==2:
                        move=Move(playerClicks[0],playerClicks[1],gs.board,isCastleMove=True)
                    if gs.epsPossible!=():
                        move=Move(playerClicks[0],playerClicks[1],gs.board,True)
                    if (gs.whiteToMove and move.pcMoved in WHITE_PIECES) or ((not gs.whiteToMove) and move.pcMoved in BLACK_PIECES):
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                gs.makeMove(move)
                                vmMade=True
                                sqSelected=()
                                playerClicks=[]
                        if not vmMade:
                            playerClicks=[sqSelected]
                            continue
        if vmMade:
            validMoves=gs.getValidMoves()
            vmMade=False
        clock.tick(MAX_FPS)
        p.display.flip()

if __name__=="__main__":
    main()