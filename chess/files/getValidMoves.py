from . import validMoves as vm

def getAllPossibleMoves(gs):
    posMoves=[]
    for row in range(8):
        for col in range(8):
            pc=gs.board[row][col]
            if (pc[0]=="w" and gs.whiteToMove) or (pc[0]=="b" and not gs.whiteToMove):
                movesFunctions={"p":vm.getPawnMoves,"R":vm.getRookMoves,"B":vm.getBishopMoves,"Q":vm.getQueenMoves,"N":vm.getNightMoves}
                if pc[1]=="K":
                    vm.getKingMoves(row,col,gs,posMoves)
                else:
                    movesFunctions[pc[1]](row,col,gs,posMoves)
    return posMoves