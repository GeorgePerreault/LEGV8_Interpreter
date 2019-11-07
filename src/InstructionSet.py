from src.MathOps import *
from src.MemOps import Load, Store
from src.BranchOps import *

# Self-explanatory
literally_just_getting_rid_of_the_wildcard_import_warning = Op()

# These tell you what subscript of the instruction set the func or params are
FUNC = 0
PARAMS = 1

# Token type constants
class TTS:
    COMMA = 0
    REGISTER = 1
    IMMEDIATE = 2
    LABEL = 3
    OPEN_SQUARE = 4
    CLOSE_SQUARE = 5
    HASH = 6

# Used for error printing
TOKEN_TYPE_NAMES = (
    "COMMA",
    "REGISTER",
    "IMMEDIATE",
    "LABEL",
    "OPEN_SQUARE",
    "CLOSE_SQUARE",
    "HASH"
)

# Currenty every instruction is in one of these forms
# Declaring them here saves space
r_r_r = (TTS.REGISTER, TTS.COMMA, TTS.REGISTER, TTS.COMMA, TTS.REGISTER)
r_r_i = (TTS.REGISTER, TTS.COMMA, TTS.REGISTER, TTS.COMMA, TTS.HASH, TTS.IMMEDIATE)
mem = (TTS.REGISTER, TTS.COMMA, TTS.OPEN_SQUARE, TTS.REGISTER, TTS.COMMA, TTS.HASH, TTS.IMMEDIATE, TTS.CLOSE_SQUARE)
br = (TTS.LABEL,)
reg = (TTS.REGISTER,)
cbr = (TTS.REGISTER, TTS.COMMA, TTS.LABEL)

INSTRUCTION_SET = {
    "add": (Add(), r_r_r),
    "addi": (Add(), r_r_i),
    "adds": (Add(s=True), r_r_r),
    "addis": (Add(s=True), r_r_i),

    "sub": (Sub(), r_r_r),
    "subi": (Sub(), r_r_i),
    "subs": (Sub(s=True), r_r_r),
    "subis": (Sub(s=True), r_r_i),

    "and": (And(), r_r_r),
    "andi": (And(), r_r_i),

    "or": (Or(), r_r_r),
    "ori": (Or(), r_r_i),

    "eor": (Eor(), r_r_r),
    "eori": (Eor(), r_r_i),

    "lsl": (LeftShift(), r_r_i),
    "lsr": (RightShift(), r_r_i),

    "ldur": (Load(), mem),
    "ldurw": (Load(n_bytes=4), mem),
    "ldurh": (Load(n_bytes=2), mem),
    "ldurb": (Load(n_bytes=1), mem),

    "stur": (Store(), mem),
    "sturw": (Store(n_bytes=4), mem),
    "sturh": (Store(n_bytes=2), mem),
    "sturb": (Store(n_bytes=1), mem),

    "b": (BranchOp(), br),
    "cbz": (CondBranch(condition=lambda x: x == 0), cbr),
    "cbnz": (CondBranch(condition=lambda x: x != 0), cbr),

    "bl": (BranchLink(), br),
    "br": (BranchReg(), reg),

    "b.eq": (BranchEQ(), br),
    "b.ne": (BranchNE(), br),
    "b.hs": (BranchHS(), br),
    "b.lo": (BranchLO(), br),
    "b.mi": (BranchMI(), br),
    "b.pl": (BranchPL(), br),
    "b.vs": (BranchVS(), br),
    "b.vc": (BranchVC(), br),
    "b.hi": (BranchHI(), br),
    "b.ls": (BranchLS(), br),
    "b.ge": (BranchGE(), br),
    "b.lt": (BranchLT(), br),
    "b.gt": (BranchGT(), br),
    "b.le": (BranchLE(), br)
}