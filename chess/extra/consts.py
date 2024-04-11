import files.validMoves as vm

WIDTH=HEIGHT=512
DIMENSION=8
SQ_SIZE=HEIGHT//DIMENSION
MAX_FPS=15
IMAGES={}
WHITE_PIECES=["wR","wN","wB","wQ","wK","wp"]
BLACK_PIECES=["bR","bN","bB","bQ","bK","bp"]
BLACK_KING=(0,4)
WHITE_KING=(7,4)
BRD_LIGHT_COLOR="#ffffff"
BRD_DARK_COLOR="#666666"
SQ_SELECTED_COLOR="#00f0f0"
SQ_SELECTED_MOVES_COLOR="#00f060"
LAST_MOVE_COLOR="#f03030"
BKS_CASTLE=True
WKS_CASTLE=True
BQS_CASTLE=True
WQS_CASTLE=True
FRAMES_PER_SQPCANIMATION=2
IA_DEPTH=3
WHITE_HUMAN=False
BLACK_HUMAN=False
PC_VALUES={
    "p":1,
    "R":5,
    "N":3,
    "B":3,
    "Q":9,
}