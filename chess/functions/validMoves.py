from classes.move import Move
def addVM(sr,sc,er,ec,bd,ms,eptMv=False,isCastleMove=False):
    ms.append(Move((sr, sc), (er, ec), bd,eptMv,isCastleMove))

def getPawnMoves(row,col,gs,vMoves):
    if gs.whiteToMove and gs.board[row][col][0]=="w": 
        if gs.board[row-1][col]=="--":
            if gs.board[row-2][col]=="--":
                addVM(row,col,row-2,col,gs.board,vMoves)
            addVM(row,col,row-1,col,gs.board,vMoves)
        if col<7:
            if gs.board[row-1][col+1][0]=="b":
                addVM(row,col,row-1,col+1,gs.board,vMoves)
            elif (row-1,col+1)==gs.epsPossible:
                addVM(row,col,row-1,col+1,gs.board,vMoves,True)
        if col>0:
            if gs.board[row-1][col-1][0]=="b":
                addVM(row,col,row-1,col-1,gs.board,vMoves)
            elif (row-1,col-1)==gs.epsPossible:
                addVM(row,col,row-1,col-1,gs.board,vMoves,True)
    elif (not gs.whiteToMove) and gs.board[row][col]=="bp":
        if gs.board[row+1][col]=="--":
            if gs.board[row+2][col]=="--":
                addVM(row,col,row+2,col,gs.board,vMoves)
            addVM(row,col,row+1,col,gs.board,vMoves)
        if col<7:
            if gs.board[row+1][col+1][0]=="w":
                addVM(row,col,row+1,col+1,gs.board,vMoves)
            elif (row+1,col+1)==gs.epsPossible:
                addVM(row,col,row+1,col+1,gs.board,vMoves,True)
        if col>0:
            if gs.board[row+1][col-1][0]=="w":
                addVM(row,col,row+1,col-1,gs.board,vMoves)
            elif (row+1,col-1)==gs.epsPossible:
                addVM(row,col,row+1,col-1,gs.board,vMoves,True)
def getRookMoves(row,col,gs,vMoves):
    enc="b" if gs.whiteToMove else "w"
    dirs=((-1,0),(0,-1),(1,0),(0,1))
    for d in dirs:
        for i in range(1,8):
            edRow=row+d[0]*i
            edCol=col+d[1]*i
            if 0<=edRow and edRow<8 and 0<=edCol and edCol<8:
                edpc=gs.board[edRow][edCol]
                if edpc=="--":
                    addVM(row,col,edRow,edCol,gs.board,vMoves)
                elif edpc[0]==enc:
                    addVM(row,col,edRow,edCol,gs.board,vMoves)
                    break
                else:
                    break
            else:
                break
def getNightMoves(row,col,gs,vMoves):
    alyc="w" if gs.whiteToMove else "b"
    dirs=((-2,-1),(-2,1),(-1,2),(-1,-2),(1,-2),(1,2),(2,-1),(2,1))
    for d in dirs:
        edRow=row+d[0]
        edCol=col+d[1]
        if 0<=edRow and edRow<8 and edCol>=0 and edCol<8:
            if gs.board[edRow][edCol][0]!=alyc:
                addVM(row,col,edRow,edCol,gs.board,vMoves)
def getBishopMoves(row,col,gs,vMoves):
    enc="b" if gs.whiteToMove else "w"
    dirs=((1,1),(-1,1),(-1,-1),(1,-1))
    for d in dirs:
        for i in range(1,8):
            edRow=row+d[0]*i
            edCol=col+d[1]*i
            if 0<=edRow and edRow<8 and 0<=edCol and edCol<8:
                edpc=gs.board[edRow][edCol]
                if edpc=="--":
                    addVM(row,col,edRow,edCol,gs.board,vMoves)
                elif edpc[0]==enc:
                    addVM(row,col,edRow,edCol,gs.board,vMoves)
                    break
                else:
                    break
            else:
                break
def getQueenMoves(row,col,gs,vMoves):
    getBishopMoves(row,col,gs,vMoves)
    getRookMoves(row,col,gs,vMoves)
def getKingMoves(row,col,gs,vMoves):
    alyc="b" if not gs.whiteToMove else "w"
    dirs=((-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,1),(-1,-1),(1,-1))
    for d in range(8):
        edRow=row+dirs[d][0]
        edCol=col+dirs[d][1]
        if 0<=edRow and edRow<8 and edCol>=0 and edCol<8:
            edSq=gs.board[edRow][edCol]
            if edSq!=alyc:
                addVM(row,col,edRow,edCol,gs.board,vMoves)
def getCastleMoves(row,col,gs,vMoves):
    if gs.sqUnderAttack((row,col)):
        return None
    if (gs.whiteToMove and gs.curCastlingRights.wks) or ((not gs.whiteToMove) and gs.curCastlingRights.bks):
        if gs.board[row][col+1]=="--" and gs.board[row][col+2]=="--":
            if (not gs.sqUnderAttack((row,col+1))) and not gs.sqUnderAttack((row,col+2)):
                addVM(row,col,row,col+2,gs.board,vMoves,isCastleMove=True)
    if (gs.whiteToMove and gs.curCastlingRights.wqs) or ((not gs.whiteToMove) and gs.curCastlingRights.bqs):
        if gs.board[row][col-1]=="--" and gs.board[row][col-2]=="--" and gs.board[row][col-3]=="--":
            if (not gs.sqUnderAttack((row,col-1))) and not gs.sqUnderAttack((row,col-2)):
                addVM(row,col,row,col-2,gs.board,vMoves,isCastleMove=True)
    return