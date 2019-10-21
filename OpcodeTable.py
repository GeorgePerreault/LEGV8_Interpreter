from MathOps import Add, Sub, And, Or, Eor, LeftShift, RightShift
from MemOps import Load, Store
from BranchOps import *

OPCODE_TABLE = {
    "add": Add(),
    "addi": Add(),
    "adds": Add(s=True),
    "addis": Add(s=True),

    "sub": Sub(),
    "subi": Sub(),
    "subs": Sub(s=True),
    "subis": Sub(s=True),

    "and": And(),
    "andi": And(),

    "or": Or(),
    "ori": Or(),

    "eor": Eor(),
    "eori": Eor(),

    "lsl": LeftShift(),
    "lsr": RightShift(),

    "ldur": Load(),
    "ldurw": Load(n_bytes=4),
    "ldurh": Load(n_bytes=2),
    "ldurb": Load(n_bytes=1),

    "stur": Store(),
    "sturw": Store(n_bytes=4),
    "sturh": Store(n_bytes=2),
    "sturb": Store(n_bytes=1),

    "b": BranchOp(),
    "cbz": CondBranch(condition=lambda x: x == 0),
    "cbnz": CondBranch(condition=lambda x: x != 0),

    "bl": BranchLink(),
    "br": BranchReg(),

    "b.eq": BranchEQ(),
    "b.ne": BranchNE(),
    "b.hs": BranchHS(),
    "b.lo": BranchLO(),
    "b.mi": BranchMI(),
    "b.pl": BranchPL(),
    "b.vs": BranchVS(),
    "b.vc": BranchVC(),
    "b.hi": BranchHI(),
    "b.ls": BranchLS(),
    "b.ge": BranchGE(),
    "b.lt": BranchLT(),
    "b.gt": BranchGT(),
    "b.le": BranchLE()
}