import pygame as p
from files.gameState import GameState
from files.move import Move
from files.animateMove import animateMove
from files.hightLightSQ import hightLightSQ
from files.drawText import drawText
from extra.consts import WIDTH,HEIGHT,MAX_FPS,SQ_SIZE,WHITE_PIECES,BLACK_PIECES,WKS_CASTLE,WQS_CASTLE,BKS_CASTLE,BQS_CASTLE,WHITE_HUMAN,BLACK_HUMAN
from files.loadImages import loadImages
from files.drawBoard import drawBoard
from chessia.funcs import findRandomMove,findBestMove,findBestMoveAGL
from files.drawPieces import drawPieces

gs=GameState()
def main():
    global BKS_CASTLE,BQS_CASTLE,WKS_CASTLE,WQS_CASTLE,gs
    p.init()
    screen=p.display.set_mode((WIDTH,HEIGHT))
    clock=p.time.Clock()
    validMoves=gs.getValidMoves()
    vmMade=False
    loadImages(gs)
    running=True
    gameOver=False
    animate=False
    sqSelected=()
    playerClicks=[]
    while running:
        humanTurn=(gs.whiteToMove and WHITE_HUMAN)or(not gs.whiteToMove and BLACK_HUMAN)
        drawBoard(screen)
        hightLightSQ(screen,gs,validMoves,sqSelected)
        drawPieces(screen,gs.board)
        for e in p.event.get():
            if e.type==p.QUIT:
                running=False
            elif e.type==p.MOUSEBUTTONDOWN:
                if not gameOver and humanTurn:
                    location=p.mouse.get_pos()
                    col=location[0]//SQ_SIZE
                    row=location[1]//SQ_SIZE
                    if sqSelected==(row,col):
                        playerClicks=[sqSelected]
                    else:
                        sqSelected=(row,col)
                        if (len(playerClicks)==1 and gs.whiteToMove and gs.board[row][col][0]=="w") or (len(playerClicks)==1 and gs.board[row][col][0]=="b" and not gs.whiteToMove):
                            playerClicks=[sqSelected]
                            continue
                        if (gs.board[row][col]=="--" and len(playerClicks)==0) or (gs.board[row][col][0]=="b" and gs.whiteToMove and len(playerClicks)==0) or (gs.board[row][col][0]=="w" and len(playerClicks)==0 and not gs.whiteToMove):
                            sqSelected=()
                            playerClicks=[]
                            continue
                        else:
                            playerClicks.append(sqSelected)
                        if len(playerClicks)==2:
                            move=Move(playerClicks[0],playerClicks[1],gs.board)
                            if gs.epsPossible!=():
                                move=Move(playerClicks[0],playerClicks[1],gs.board,epMv=True)
                            if (gs.whiteToMove and move.pcMoved in WHITE_PIECES) or ((not gs.whiteToMove) and move.pcMoved in BLACK_PIECES):
                                for i in range(len(validMoves)):
                                    if move == validMoves[i]:
                                        gs.makeMove(move)
                                        vmMade=True
                                        sqSelected=()
                                        animate=True
                                        playerClicks=[]
                                if not vmMade:
                                    sqSelected=()
                                    playerClicks=[]
                                    continue
            elif e.type==p.KEYDOWN:
                if e.key == p.K_z:
                    animate=False
                    gs.undoMove()
                    humanTurn=(gs.whiteToMove and WHITE_HUMAN)or(not gs.whiteToMove and BLACK_HUMAN)
                    sqSelected=()
                    playerClicks=[]
                    gameOver=False
                    vmMade=True
                if e.key==p.K_r:
                    animate=False
                    gameOver=False
                    BKS_CASTLE,BQS_CASTLE,WKS_CASTLE,WQS_CASTLE=True,True,True,True
                    gs=GameState()
                    validMoves=gs.getValidMoves()
                    sqSelected=()
                    playerClicks=[]
                    gameOver=False
                    vmMade=False
                    gs.checkMate=False
                    gs.staleMate=False
        if not gameOver and not humanTurn:
            AIMv=findBestMoveAGL(gs,validMoves)
            if AIMv==None:
                AIMv=findRandomMove(validMoves)
            gs.makeMove(AIMv)
            vmMade=True
            animate=True
        if vmMade:
            if animate:
                animateMove(gs.moveLog[-1],screen,gs,clock)
            validMoves=gs.getValidMoves()
            vmMade=False
        clock.tick(MAX_FPS)
        if gs.checkMate:
            gameOver=True
            if gs.whiteToMove:
                drawText(screen,"Black wins by checkmate")
            else:
                drawText(screen,"White wins by checkmate")
        elif gs.staleMate:
            gameOver=True
            drawText(screen,"Draw by stalemate")
        p.display.flip()

if __name__=="__main__":
    main()