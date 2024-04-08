
class Move:
    ranksToRows = {8:0,7:1,6:2,5:3,4:4,3:5,2:6,1:7}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0,"b": 1,"c": 2,"d": 3,"e": 4,"f": 5,"g": 6,"h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    def __init__(self,startSq,endSq,board,epMv=False):
        self.stRow=startSq[0]
        self.stCol=startSq[1]
        self.edRow=endSq[0]
        self.edCol=endSq[1]
        self.pcMoved=board[self.stRow][self.stCol]
        self.pcCaptured=board[self.edRow][self.edCol]
        self.moveId=self.stRow*1000+self.stCol*100+self.edRow*10+self.edCol
        self.isPawnPromotion=(self.pcMoved=="wp" and self.edRow==0)or(self.pcMoved=="bp" and self.edRow==7)
        self.epMv=epMv
        self.isCastleMove=False
        if self.pcMoved[1]=="K" and abs(self.edCol-self.stCol)==2:
            self.isCastleMove=True
        if epMv:
            self.pcCaptured="wp" if self.pcMoved=="bp" else "bp"
        if self.edCol==self.stCol and self.pcMoved[1]=="p":
            self.pcCaptured="--"
    def __str__(self):
        if self.pcCaptured!="--":
            return f"{self.pcMoved}{self.getRankFile(self.stCol,self.stRow)}x{self.pcCaptured}{self.getRankFile(self.edCol,self.edRow)}"
        return f"{self.pcMoved}{self.getRankFile(self.stCol,self.stRow)}{self.getRankFile(self.edCol,self.edRow)}"
    def __eq__(self,other):
        if isinstance(other,Move):
            return self.moveId==other.moveId
        return False
    def getRankFile(self,col,row):
        return str(self.colsToFiles[col])+str(self.rowsToRanks[row])