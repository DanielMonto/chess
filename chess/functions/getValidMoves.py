from . import validMoves as vm
from extra.consts import WHITE_KING,BLACK_KING
from classes.castlingRights import CastlingRights

def getAllPossibleMoves(gs):
    posMoves=[]
    for row in range(8):
        for col in range(8):
            pc=gs.board[row][col]
            if (pc[0]=="w" and gs.whiteToMove) or (pc[0]=="b" and not gs.whiteToMove):
                movesFunctions={"p":vm.getPawnMoves,"R":vm.getRookMoves,"B":vm.getBishopMoves,"Q":vm.getQueenMoves,"N":vm.getNightMoves,"K":vm.getKingMoves,}
                movesFunctions[pc[1]](row,col,gs,posMoves)
    return posMoves
def getValidMoves(gs):
    tEptPos=gs.epsPossible
    tCastlingRights=CastlingRights(gs.curCastlingRights.wks,gs.curCastlingRights.wqs,gs.curCastlingRights.bks,gs.curCastlingRights.bqs)
    VM=getAllPossibleMoves(gs)
    if gs.whiteToMove:
        vm.getCastleMoves(WHITE_KING[0],WHITE_KING[1],gs,VM)
    else:
        vm.getCastleMoves(BLACK_KING[0],BLACK_KING[1],gs,VM)
    for i in range(len(VM)-1,-1,-1):
        gs.makeMove(VM[i])
        gs.unTurn()
        if gs.inCheck():
            VM.remove(VM[i])
        gs.unTurn()
        gs.undoMove()
    if len(VM)==0:
        if gs.inCheck():
            gs.ckMt(True)
        else:
            gs.stMt(True)
    else:
        gs.ckMt(False)
        gs.stMt(False)
    gs.setEpsPos(tEptPos)
    gs.setCastlingRights(tCastlingRights)
    return VM