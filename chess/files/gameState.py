from extra.consts import INITIAL_BOARD,WHITE_KING,BLACK_KING,BKS_CASTLE,BQS_CASTLE,WKS_CASTLE,WQS_CASTLE
from .move import Move
from .getValidMoves import getAllPossibleMoves

class GameState:
    def __init__(self):
        self.board=INITIAL_BOARD
        self.whiteToMove=True
        self.moveLog=[]
        self.rightCastleLog=[(BKS_CASTLE,BQS_CASTLE,WKS_CASTLE,WQS_CASTLE)]
        self.checkMate=False
        self.staleMate=False
        self.epsPossible=()
    def setEpsPos(self,p):
        self.epsPossible=p
    def ckMt(self,p):
        self.checkMate=p
    def stMt(self,p):
        self.staleMate=p
    def makeMove(self,move:Move):
        global WHITE_KING,BLACK_KING,BKS_CASTLE,BQS_CASTLE,WKS_CASTLE,WQS_CASTLE
        self.board[move.edRow][move.edCol]=move.pcMoved
        self.board[move.stRow][move.stCol]="--"
        self.moveLog.append(move)
        self.whiteToMove=not self.whiteToMove
        if move.isCastleMove:
            if move.stRow==0:
                if move.edCol==6:
                    self.board[0][5]="bR"
                    self.board[0][7]="--"
                elif move.edCol==2:
                    self.board[0][3]="bR"
                    self.board[0][0]="--"
            elif move.stRow==7:
                if move.edCol==6:
                    self.board[7][5]="wR"
                    self.board[7][7]="--"
                elif move.edCol==2:
                    self.board[7][3]="wR"
                    self.board[7][0]="--"
        if move.pcMoved=="wK":
            WKS_CASTLE=False
            WQS_CASTLE=False
            WHITE_KING=(move.edRow,move.edCol)
        elif move.pcMoved=="bK":
            BKS_CASTLE=False
            BQS_CASTLE=False
            BLACK_KING=(move.edRow,move.edCol)
        if move.isPawnPromotion:
            self.board[move.edRow][move.edCol]=move.pcMoved[0]+"Q"
        if move.epMv:
            self.board[move.stRow][move.edCol]="--"
        if move.pcMoved[1]=="p" and abs(move.stRow-move.edRow)==2:
            self.epsPossible=((move.stRow+move.edRow)//2,move.edCol)
        else:
            self.epsPossible=()
        if move.pcMoved[1]=="R" and (BKS_CASTLE or BQS_CASTLE or WKS_CASTLE or WQS_CASTLE):
            if move.stRow==7:
                if move.stCol==7:
                    WKS_CASTLE=False
                elif move.stCol==0:
                    WQS_CASTLE=False
            elif move.stRow==0:
                if move.stCol==7:
                    BKS_CASTLE=False
                elif move.stCol==0:
                    BQS_CASTLE=False
        self.rightCastleLog.append((BKS_CASTLE,BQS_CASTLE,WKS_CASTLE,WQS_CASTLE))
    def unTurn(self):
        self.whiteToMove=not self.whiteToMove
    def undoMove(self):
        global WHITE_KING,BLACK_KING,BKS_CASTLE,BQS_CASTLE,WKS_CASTLE,WQS_CASTLE
        if len(self.moveLog)>0:
            move=self.moveLog.pop()
            self.rightCastleLog.pop()
            BKS_CASTLE,BQS_CASTLE,WKS_CASTLE,WQS_CASTLE=self.rightCastleLog[-1]
            self.board[move.stRow][move.stCol]=move.pcMoved
            self.board[move.edRow][move.edCol]=move.pcCaptured
            self.whiteToMove=not self.whiteToMove
            if move.pcMoved[1]=="p" and abs(move.edRow-move.stRow)==2:
                self.epsPossible=()
            if move.epMv:
                self.board[move.edRow][move.edCol]="--"
                self.board[move.stRow][move.edCol]=move.pcCaptured
            if move.pcMoved=="wK":
                WHITE_KING=(move.stRow,move.stCol)
            elif move.pcMoved=="bK":
                BLACK_KING=(move.stRow,move.stCol)
            if move.isCastleMove:
                if move.stRow==0:
                    if move.edCol==6:
                        self.board[0][5]="--"
                        self.board[0][7]="bR"
                    elif move.edCol==2:
                        self.board[0][3]="--"
                        self.board[0][0]="bR"
                elif move.stRow==7:
                    if move.edCol==6:
                        self.board[7][5]="--"
                        self.board[7][7]="wR"
                    elif move.edCol==2:
                        self.board[7][3]="--"
                        self.board[7][0]="wR"
            if len(self.moveLog)>0:
                if (move.pcMoved[1]=="p" and move.stCol==move.edCol):
                    self.board[move.stRow][move.stCol]="wp" if self.whiteToMove else "bp"
                    self.board[move.edRow][move.edCol]="--"
    def sqUnderAttack(self,sq):
        self.whiteToMove=not self.whiteToMove
        oppMVS=getAllPossibleMoves(self)
        self.whiteToMove=not self.whiteToMove
        for mv in oppMVS:
            if mv.edRow==sq[0] and mv.edCol==sq[1]:
                return True
        return False
    def inCheck(self):
        return self.sqUnderAttack(WHITE_KING) if self.whiteToMove else self.sqUnderAttack(BLACK_KING)
    def getCastleMoves(self,vml):
        curK=WHITE_KING if self.whiteToMove else BLACK_KING
        if self.sqUnderAttack(curK):
            return
        if curK==WHITE_KING:
            if WKS_CASTLE:
                if (self.board[curK[0]][curK[1]+1]=="--" and not self.sqUnderAttack((curK[0],curK[1]+1))) and self.board[curK[0]][curK[1]+2]=="--" and  not self.sqUnderAttack((curK[0],curK[1]+2)):
                    vml.append(Move(curK,(curK[0],curK[1]+2),self.board))
            if WQS_CASTLE:
                if (not self.sqUnderAttack((curK[0],curK[1]-1))) and not self.sqUnderAttack((curK[0],curK[1]-2)) and self.board[curK[0]][curK[1]-3]=="--" and self.board[curK[0]][curK[1]-2]=="--" and self.board[curK[0]][curK[1]-1]=="--":
                    vml.append(Move(curK,(curK[0],curK[1]-2),self.board))
        elif curK==BLACK_KING:
            if BKS_CASTLE:
                if (not self.sqUnderAttack((curK[0],curK[1]+1))) and not self.sqUnderAttack((curK[0],curK[1]+2)) and self.board[curK[0]][curK[1]+2]=="--" and self.board[curK[0]][curK[1]+1]=="--":
                    vml.append(Move(curK,(curK[0],curK[1]+2),self.board))
            if BQS_CASTLE:
                if (not self.sqUnderAttack((curK[0],curK[1]-1))) and not self.sqUnderAttack((curK[0],curK[1]-2)) and self.board[curK[0]][curK[1]-3]=="--" and self.board[curK[0]][curK[1]-2]=="--" and self.board[curK[0]][curK[1]-1]=="--":
                    vml.append(Move(curK,(curK[0],curK[1]-2),self.board))
    def getValidMoves(self):
        global BKS_CASTLE,BQS_CASTLE,WKS_CASTLE,WQS_CASTLE
        tEptPos=self.epsPossible
        tCastleRights=WKS_CASTLE,WQS_CASTLE,BKS_CASTLE,BQS_CASTLE
        VM=getAllPossibleMoves(self)
        for i in range(len(VM)-1,-1,-1):
            self.makeMove(VM[i])
            self.unTurn()
            if self.inCheck():
                VM.remove(VM[i])
            self.unTurn()
            self.undoMove()
        if len(VM)==0:
            if self.inCheck():
                self.ckMt(True)
            else:
                self.stMt(True)
        else:
            self.ckMt(False)
            self.stMt(False)
        self.epsPossible=tEptPos
        WKS_CASTLE,WQS_CASTLE,BKS_CASTLE,BQS_CASTLE=tCastleRights
        self.getCastleMoves(VM)
        return VM