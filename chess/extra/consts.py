import files.validMoves as vm

WIDTH=HEIGHT=512
DIMENSION=8
SQ_SIZE=HEIGHT//DIMENSION
MAX_FPS=15
IMAGES={}
INITIAL_BOARD=[
    ["bR","bN","bB","bQ","bK","bB","bN","bR"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wR","wN","wB","wQ","wK","wB","wN","wR"]
]
WHITE_PIECES=["wR","wN","wB","wQ","wK","wp"]
BLACK_PIECES=["bR","bN","bB","bQ","bK","bp"]
BLACK_KING=(0,4)
WHITE_KING=(7,4)
BRD_LIGHT_COLOR="white"
BRD_DARK_COLOR="gray"
SQ_SELECTED_COLOR="blue"
SQ_SELECTED_MOVES_COLOR="yellow"
BKS_CASTLE=True
WKS_CASTLE=True
BQS_CASTLE=True
WQS_CASTLE=True