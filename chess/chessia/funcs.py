import random
from extra.consts import PC_VALUES,IA_DEPTH

CHECKMATE=999999
STALEMATE=0

def findRandomMove(vms):
    return vms[random.randint(0,len(vms)-1)]
def scoreMaterial(board):
    evaluation=0
    for row in range(8):
        for col in range(8):
            pc=board[row][col]
            if pc[1]!="K":
                if pc[0]=="w":
                    evaluation+=PC_VALUES[pc[1]]
                elif pc[0]=="b":
                    evaluation-=PC_VALUES[pc[1]]
    return evaluation
def scoreBoard(gs):
    if gs.checkMate:
        if gs.whiteToMove:
            return -CHECKMATE
        elif not gs.whiteToMove:
            return CHECKMATE
    elif gs.staleMate:
        return STALEMATE
    evaluation=0
    for row in range(8):
        for col in range(8):
            pc=gs.board[row][col]
            if pc[1]!="K":
                if pc[0]=="w":
                    evaluation+=PC_VALUES[pc[1]]
                elif pc[0]=="b":
                    evaluation-=PC_VALUES[pc[1]]
    return evaluation
def findBestMove(gs, vms):
    turnMultiplier = 1 if gs.whiteToMove else -1
    oppMinMaxScore = CHECKMATE
    bestPlayerMove = None
    random.shuffle(vms)
    for mv in vms:
        gs.makeMove(mv)
        oppMoves = gs.getValidMoves()
        if gs.staleMate:
            oppMaxScore = STALEMATE
        elif gs.checkMate:
            oppMaxScore = -CHECKMATE
        else:
            oppMaxScore = -CHECKMATE
            for oppMv in oppMoves:
                gs.makeMove(oppMv)
                playerMoves = gs.getValidMoves()
                playerMaxScore = -CHECKMATE
                for playerMv in playerMoves:
                    gs.makeMove(playerMv)
                    score = -turnMultiplier * scoreMaterial(gs.board)
                    playerMaxScore = max(playerMaxScore, score)
                    gs.undoMove()
                oppMaxScore = max(oppMaxScore, playerMaxScore)
                gs.undoMove()
        if oppMaxScore < oppMinMaxScore:
            oppMinMaxScore = oppMaxScore
            bestPlayerMove = mv
        gs.undoMove()
    return bestPlayerMove
def findBestMoveAGL(gs,vms):
    global nextMove
    nextMove=None
    depth=IA_DEPTH
    random.shuffle(vms)
    findMoveNegaMaxAlphaBeta(gs,vms,depth,1 if gs.whiteToMove else -1,-CHECKMATE,CHECKMATE)
    return nextMove
def findMoveMinMax(gs,vms,depth,wToMove):
    global nextMove
    if depth==0:
        return scoreBoard(gs)
    if wToMove:
        maxScore=-CHECKMATE
        for mv in vms:
            gs.makeMove(mv)
            nextMoves=gs.getValidMoves()
            score=findMoveMinMax(gs,nextMoves,depth-1,False)
            if score>maxScore:
                maxScore=score
                if depth==IA_DEPTH:
                    nextMove=mv
            gs.undoMove()
        return maxScore
    else:
        minScore=CHECKMATE
        for mv in vms:
            gs.makeMove(mv)
            nextMoves=gs.getValidMoves()
            score=findMoveMinMax(gs,nextMoves,depth-1,True)
            if score<minScore:
                minScore=score
                if depth==IA_DEPTH:
                    nextMove=mv
            gs.undoMove()
        return minScore
def findMoveNegaMax(gs,vms,depth,turnMultiplier):
    global nextMove
    if depth==0:
        return turnMultiplier*scoreBoard(gs)
    maxScore=-CHECKMATE
    for mv in vms:
        gs.makeMove(mv)
        nextMoves=gs.getValidMoves()
        score=-findMoveNegaMax(gs,nextMoves,depth-1,-turnMultiplier)
        if score>maxScore:
            maxScore=score
            if depth==IA_DEPTH:
                nextMove=mv
        gs.undoMove()
    return maxScore
def findMoveNegaMaxAlphaBeta(gs,vms,depth,turnMultiplier,alpha,beta):
    global nextMove
    if depth==0:
        return turnMultiplier*scoreBoard(gs)
    maxScore=-CHECKMATE
    for mv in vms:
        gs.makeMove(mv)
        nextMoves=gs.getValidMoves()
        score=-findMoveNegaMaxAlphaBeta(gs,nextMoves,depth-1,-turnMultiplier,-beta,-alpha)
        if score>maxScore:
            maxScore=score
            if depth==IA_DEPTH:
                nextMove=mv
        gs.undoMove()
        if maxScore>alpha:
            alpha=maxScore
        if alpha>=beta:
            break
    return maxScore