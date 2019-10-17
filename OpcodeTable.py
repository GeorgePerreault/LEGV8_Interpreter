from MathOps import Add, Sub, And, Or, Eor
from MemOps import Load, Store
from BranchOps import *
from ShiftOps import LeftShift, RightShift

class OpcodeTable():

    def __init__(self, cpu):
        self.OPCODE_TABLE = {
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

            "ldur": Load(cpu),
            "ldurw": Load(cpu, n_bytes=4),
            "ldurh": Load(cpu, n_bytes=2),
            "ldurb": Load(cpu, n_bytes=1),

            "stur": Store(cpu),
            "sturw": Store(cpu, n_bytes=4),
            "sturh": Store(cpu, n_bytes=2),
            "sturb": Store(cpu, n_bytes=1),

            "b": BranchOp(cpu),
            "cbz": BranchOp(cpu, condition=lambda x: x == 0),
            "cbnz": BranchOp(cpu, condition=lambda x: x != 0),

            "bl": None,
            "br": None,

            "b.eq": BranchEQ(cpu),
            "b.ne": BranchNE(cpu),
            "b.hs": BranchHS(cpu),
            "b.lo": BranchLO(cpu),
            "b.mi": BranchMI(cpu),
            "b.pl": BranchPL(cpu),
            "b.vs": BranchVS(cpu),
            "b.hi": BranchHI(cpu),
            "b.ls": BranchLS(cpu),
            "b.ge": BranchGE(cpu),
            "b.lt": BranchLT(cpu),
            "b.gt": BranchGT(cpu),
            "b.le": BranchLE(cpu),
        }

    def __getitem__(self, i):
        return self.OPCODE_TABLE[i]

    def __setitem__(self, i, v):
        raise Exception("Don't set item on the opcode table")