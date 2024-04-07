from extra.consts import INITIAL_BOARD,WHITE_KING,BLACK_KING
from .move import Move
from .castlingRights import CastlingRights
from functions.getValidMoves import getAllPossibleMoves

class GameState:
    def __init__(self):
        self.board=INITIAL_BOARD
        self.whiteToMove=True
        self.moveLog=[]
        self.checkMate=False
        self.staleMate=False
        self.epsPossible=()
        self.curCastlingRights=CastlingRights(True,True,True,True)
        self.castleRightLog=[CastlingRights(self.curCastlingRights.wks,self.curCastlingRights.wqs,self.curCastlingRights.bks,self.curCastlingRights.bqs)]
    def setEpsPos(self,p):
        self.epsPossible=p
    def ckMt(self,p):
        self.checkMate=p
    def stMt(self,p):
        self.staleMate=p
    def makeMove(self,move:Move):
        global WHITE_KING,BLACK_KING
        self.board[move.edRow][move.edCol]=move.pcMoved
        self.board[move.stRow][move.stCol]="--"
        self.moveLog.append(move)
        self.whiteToMove=not self.whiteToMove
        if move.isCastleMove:
            print(f"{move.edCol}")
            if move.edCol==6:
                print("castleMovKingside")
                self.board[move.edRow][5]="wR" if self.whiteToMove else "bR"
                self.board[move.edRow][7]="--"
            elif move.edCol==2:
                self.board[move.edRow][3]="wR" if self.whiteToMove else "bR"
                self.board[move.edRow][0]="--"
        if move.pcMoved=="wK":
            WHITE_KING=(move.edRow,move.edCol)
        elif move.pcMoved=="bK":
            BLACK_KING=(move.edRow,move.edCol)
        if move.isPawnPromotion:
            self.board[move.edRow][move.edCol]=move.pcMoved[0]+"Q"
        if move.eptMv:
            self.board[move.stRow][move.edCol]="--"
        if move.pcMoved[1]=="p" and abs(move.stRow-move.edRow)==2:
            self.epsPossible=((move.stRow+move.edRow)//2,move.stCol)
        else:
            self.epsPossible=()
        self.updateCastleRights(move)
        self.castleRightLog.append(CastlingRights(self.curCastlingRights.wks,self.curCastlingRights.wqs,self.curCastlingRights.bks,self.curCastlingRights.bqs))
    def updateCastleRights(self,move):
        if move.pcMoved[1]=="wK":
            self.curCastlingRights.wks=False
            self.curCastlingRights.wqs=False
        elif move.pcMoved[1]=="bK":
            self.curCastlingRights.bks=False
            self.curCastlingRights.bqs=False
        elif move.pcMoved=="wR":
            if move.stCol==0 and move.stRow==7:
                self.curCastlingRights.wqs=False
            elif move.stCol==7 and move.stRow==7:
                self.curCastlingRights.wks=False
        elif move.pcMoved=="bR":
            if move.stCol==0 and move.stRow==0:
                self.curCastlingRights.bqs=False
            elif move.stCol==7 and move.stRow==0:
                self.curCastlingRights.bks=False
    def setCastlingRights(self,p):
        self.curCastlingRights=CastlingRights(p.wks,p.wqs,p.bks,p.bqs)
    def unTurn(self):
        self.whiteToMove=not self.whiteToMove
    def undoMove(self):
        global WHITE_KING,BLACK_KING
        if len(self.moveLog)>0:
            move=self.moveLog.pop()
            self.board[move.stRow][move.stCol]=move.pcMoved
            self.board[move.edRow][move.edCol]=move.pcCaptured
            self.whiteToMove=not self.whiteToMove
            if move.pcMoved=="wK":
                WHITE_KING=(move.stRow,move.stCol)
            elif move.pcMoved=="bK":
                BLACK_KING=(move.stRow,move.stCol)
            if move.eptMv:
                self.board[move.edRow][move.edCol]="--"
                self.board[move.stRow][move.edCol]=move.pcCaptured
                self.epsPossible=(move.edRow,move.edCol)
            if move.pcMoved[1]=="p" and abs(move.stRow-move.edRow)==2:
                self.epsPossible=()
            self.castleRightLog.pop()
            self.curCastlingRights=self.castleRightLog[-1]
            if move.isCastleMove:
                if move.edCol==6:
                    self.board[move.edRow][move.stCol+3]=self.board[move.edRow][move.stCol+1]
                    self.board[move.edRow][move.stCol+1]="--"
                elif move.edCol==2:
                    self.board[move.edRow][move.stCol-4]=self.board[move.edRow][move.stCol-1]
                    self.board[move.edRow][move.stCol-1]="--"
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
