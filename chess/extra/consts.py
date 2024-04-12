KNIGHT_SCORES=[[1,1,2,2,2,2,1,1],
[1,3,3,3,3,3,3,1],
[2,3,4,4,4,4,3,2],
[2,3,4,5,5,4,3,2],
[2,3,4,5,5,4,3,2],
[2,3,4,4,4,4,3,2],
[1,3,3,3,3,3,3,1],
[1,1,2,2,2,2,1,1]
]
BISHOP_SCORES=[[5,4,3,1,1,3,4,5],
[4,5,4,3,3,4,5,4],
[3,4,5,4,4,5,4,3],
[1,3,4,5,5,4,3,1],
[1,3,4,5,5,4,3,1],
[3,4,5,4,4,5,4,3],
[4,5,4,3,3,4,5,4],
[5,4,3,1,1,3,4,5]
]
ROOK_SCORES=[[1,2,3,3,3,3,2,1],
[2,3,3,3,3,3,3,2],
[3,3,4,4,4,4,3,3],
[3,3,4,4,4,4,3,3],
[3,3,4,4,4,4,3,3],
[3,3,4,4,4,4,3,3],
[2,3,3,3,3,3,3,2],
[1,2,3,3,3,3,2,1],
]
QUEEN_SCORES=[[1,2,3,3,3,3,2,1],
[2,4,4,3,3,4,4,2],
[3,4,4,4,4,4,4,3],
[3,3,4,4,4,4,3,3],
[3,3,4,4,4,4,3,3],
[3,4,4,4,4,4,4,3],
[2,4,4,3,3,4,4,2],
[1,2,3,3,3,3,2,1],
]
WHITE_P_SCORES=[[8,8,8,8,8,8,8,8],
[7,7,7,8,8,7,7,7],
[6,6,6,7,7,6,6,6],
[4,4,4,5,5,4,4,4],
[1,3,3,5,5,3,3,1],
[1,2,2,3,3,2,2,1],
[1,1,1,0,0,1,1,1],
[0,0,0,0,0,0,0,0],
]
BLACK_P_SCORES=[[0,0,0,0,0,0,0,0],
[1,1,1,0,0,1,1,1],
[1,2,2,3,3,2,2,1],
[1,3,3,5,5,3,3,1],
[4,4,4,5,5,4,4,4],
[6,6,6,7,7,6,6,6],
[7,7,7,8,8,7,7,7],
[8,8,8,8,8,8,8,8]
]
KING_SCORES=[[1,1,2,0,0,1,2,1],
[0,1,1,1,1,1,0,1],
[0,1,1,1,1,1,0,2],
[0,1,1,1,1,1,0,2],
[0,1,1,1,1,1,0,2],
[0,1,1,1,1,1,0,2],
[0,0,1,1,1,1,0,1],
[1,1,2,0,0,1,2,1]
]
PC_POSITIONS_SCORES={"N":KNIGHT_SCORES,
"B":BISHOP_SCORES,
"K":KING_SCORES,
"R":ROOK_SCORES,
"Q":QUEEN_SCORES,
"wp":WHITE_P_SCORES,
"bp":BLACK_P_SCORES
}
WIDTH=HEIGHT=512
DIMENSION=8
SQ_SIZE=HEIGHT//DIMENSION
MAX_FPS=15
IMAGES={}
WHITE_PIECES=["wR",
"wN",
"wB",
"wQ",
"wK",
"wp"]
BLACK_PIECES=["bR",
"bN",
"bB",
"bQ",
"bK",
"bp"]
BLACK_KING=(0,
4)
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
BLACK_HUMAN=True
PC_VALUES={
    "p":1,
    "R":5,
    "N":3,
    "B":3,
    "Q":9,
    "K":0
}