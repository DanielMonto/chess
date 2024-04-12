from files.move import Move
def addVM(gs,sr,sc,er,ec,bd,ms,epMv=False):
    curMove=Move((sr, sc), (er, ec), bd,epMv)
    gs.makeMove(curMove)
    gs.unTurn()
    if not gs.inCheck():
        ms.append(curMove)
    gs.unTurn()
    gs.undoMove()

def getPawnMoves(row,col,gs,vMoves):
    if gs.whiteToMove and gs.board[row][col][0]=="w": 
        if gs.board[row-1][col]=="--":
            if row==6:
                if gs.board[row-2][col]=="--":
                    addVM(gs,row,col,row-2,col,gs.board,vMoves)
            addVM(gs,row,col,row-1,col,gs.board,vMoves)
        if col<7:
            if gs.board[row-1][col+1][0]=="b":
                addVM(gs,row,col,row-1,col+1,gs.board,vMoves)
            elif (row-1,col+1)==gs.epsPossible:
                if len(gs.moveLog)>0:
                    if gs.moveLog[-1].stRow==1 and abs(gs.moveLog[-1].edRow-gs.moveLog[-1].stRow)==2:
                        addVM(gs,row,col,row-1,col+1,gs.board,vMoves,epMv=True)
        if col>0:
            if gs.board[row-1][col-1][0]=="b":
                addVM(gs,row,col,row-1,col-1,gs.board,vMoves)
            elif (row-1,col-1)==gs.epsPossible:
                if len(gs.moveLog)>0:
                    if gs.moveLog[-1].stRow==1 and abs(gs.moveLog[-1].edRow-gs.moveLog[-1].stRow)==2:
                        addVM(gs,row,col,row-1,col-1,gs.board,vMoves,epMv=True)
    elif (not gs.whiteToMove) and gs.board[row][col]=="bp":
        if gs.board[row+1][col]=="--":
            if row==1:
                if gs.board[row+2][col]=="--":
                    addVM(gs,row,col,row+2,col,gs.board,vMoves)
            addVM(gs,row,col,row+1,col,gs.board,vMoves)
        if col<7:
            if gs.board[row+1][col+1][0]=="w" or (row+1,col+1)==gs.epsPossible:
                addVM(gs,row,col,row+1,col+1,gs.board,vMoves)
        if col>0:
            if gs.board[row+1][col-1][0]=="w" or (row+1,col-1)==gs.epsPossible:
                addVM(gs,row,col,row+1,col-1,gs.board,vMoves)
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
                    addVM(gs,row,col,edRow,edCol,gs.board,vMoves)
                elif edpc[0]==enc:
                    addVM(gs,row,col,edRow,edCol,gs.board,vMoves)
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
                addVM(gs,row,col,edRow,edCol,gs.board,vMoves)
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
                    addVM(gs,row,col,edRow,edCol,gs.board,vMoves)
                elif edpc[0]==enc:
                    addVM(gs,row,col,edRow,edCol,gs.board,vMoves)
                    break
                else:
                    break
            else:
                break
def getQueenMoves(row,col,gs,vMoves):
    getBishopMoves(row,col,gs,vMoves)
    getRookMoves(row,col,gs,vMoves)
def getKingMoves(row,col,gs,vMoves):
    enc="b" if gs.whiteToMove else "w"
    dirs=((-1,0),(0,-1),(1,0),(0,1),(1,1),(-1,1),(-1,-1),(1,-1))
    for d in dirs:
        edRow=row+d[0]
        edCol=col+d[1]
        if 0<=edRow and edRow<8 and edCol>=0 and edCol<8:
            edSq=gs.board[edRow][edCol]
            if edSq[0]==enc:
                curMove=Move((row, col), (edRow, edCol), gs.board)
                gs.makeMove(curMove)
                gs.unTurn()
                if not gs.sqUnderAttack((edRow,edCol)):
                    vMoves.append(curMove)
                gs.unTurn()
                gs.undoMove()